from cbuild.step import fetch, extract, patch, configure
from cbuild.step import build as buildm, check, install, prepkg, pkg as pkgsm
from cbuild.core import chroot, logger, dependencies
from cbuild.core import template, pkg as pkgm, paths, errors
from cbuild.apk import cli as apk

import os
import pathlib

def build(
    step, pkg, depmap, signkey, chost = False,
    dirty = False, keep_temp = False, check_fail = False
):
    if chost:
        depn = "host-" + pkg.pkgname
    else:
        depn = pkg.pkgname

    if depn in depmap:
        pkg.error(f"build-time dependency cycle encountered for {pkg.pkgname} (dependency of {pkg.origin.pkgname})")

    depmap[depn] = True

    pkg.install_done = False
    pkg.current_phase = "setup"

    # always clean up before starting, unless exlpicitly requested not to
    # or unless bootstrapping stage 0 (as resumption is useful by default
    # in there) but not any other stage
    if not dirty and pkg.stage > 0:
        # clean up old state
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    pkg.statedir.mkdir(parents = True, exist_ok = True)
    pkg.wrapperdir.mkdir(parents = True, exist_ok = True)

    if not dirty:
        if pkg.stage > 0:
            chroot.update()

        # doesn't do anything for native builds
        dependencies.install_toolchain(pkg, signkey)

        # we treat the sysroot as a chimera root
        dependencies.init_sysroot(pkg)

        # remove automatic crossdeps from last time
        dependencies.remove_autocrossdeps(pkg)

        # check and install dependencies
        dependencies.install(
            pkg, pkg.origin.pkgname, "pkg", depmap, signkey, chost
        )

    oldcwd = pkg.cwd
    oldchd = pkg.chroot_cwd

    pkg.cwd = pkg.builddir / pkg.wrksrc
    pkg.chroot_cwd = pkg.chroot_builddir / pkg.wrksrc

    # ensure the wrksrc exists; it will be populated later
    pkg.cwd.mkdir(exist_ok = True, parents = True)

    # run up to the step we need
    pkg.current_phase = "fetch"
    fetch.invoke(pkg)
    if step == "fetch":
        return
    pkg.current_phase = "extract"
    extract.invoke(pkg)
    if step == "extract":
        return

    pkg.current_phase = "patch"
    patch.invoke(pkg)
    if step == "patch":
        return

    pkg.cwd = oldcwd
    pkg.chroot_cwd = oldchd

    pkg.current_phase = "configure"
    configure.invoke(pkg, step)
    if step == "configure":
        return
    pkg.current_phase = "build"
    buildm.invoke(pkg, step)
    if step == "build":
        return
    pkg.current_phase = "check"
    check.invoke(pkg, step, check_fail)
    if step == "check":
        return

    # invoke install for main package
    pkg.current_phase = "install"
    install.invoke(pkg, False)

    pkg.install_done = True
    # scan for ELF information after subpackages are split up
    # but before post_install hooks (done by the install step)
    pkg.current_elfs = {}

    # handle subpackages
    for sp in pkg.subpkg_list:
        install.invoke(sp, True)

    # after subpackages are done, do the same for main package in subpkg mode
    install.invoke(pkg, True)

    pkg.current_phase = "pkg"
    template.call_pkg_hooks(pkg, "init_pkg")

    for sp in pkg.subpkg_list:
        prepkg.invoke(sp)

    prepkg.invoke(pkg)

    if step == "install":
        return

    pkg.signing_key = signkey
    pkg._stage = {}

    # generate binary packages
    for sp in pkg.subpkg_list:
        pkgsm.invoke(sp)

    pkgsm.invoke(pkg)

    # stage binary packages
    for repo in pkg._stage:
        logger.get().out(f"Staging new packages to {repo}...")
        if not apk.build_index(repo, pkg.source_date_epoch, signkey):
            raise errors.CbuildException("indexing repositories failed")

    pkg.signing_key = None

    # cleanup
    if not keep_temp:
        chroot.remove_autodeps(pkg.stage == 0)
        dependencies.remove_autocrossdeps(pkg)
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    del depmap[depn]
