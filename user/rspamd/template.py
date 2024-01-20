pkgname = "rspamd"
pkgver = "3.8.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCONFDIR=/etc/rspamd",
    "-DENABLE_FASTTEXT=ON",
    "-DENABLE_LUAJIT=OFF",
    "-DENABLE_URI_INCLUDE=ON",
    "-DRSPAMD_GROUP=_rspamd",
    "-DRSPAMD_USER=_rspamd",
    "-DSYSTEM_FMT=ON",
    "-DSYSTEM_XXHASH=ON",
    "-DSYSTEM_ZSTD=ON",
    "-D_CAN_RUN=0",
    "-DHAVE_ATOMIC_BUILTINS_EXITCODE=0",
]
make_build_args = ["--target", "all", "check"]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf", "ragel"]
makedepends = [
    "elfutils-devel",
    "fasttext-devel",
    "fmt-devel",
    "glib-devel",
    "icu-devel",
    "libsodium-devel",
    "libunwind-devel",
    "linux-headers",
    "lua5.4-devel",
    "openssl-devel",
    "pcre2-devel",
    "snowball-devel",
    "sqlite-devel",
    "xxhash-devel",
    "zstd-devel",
]
pkgdesc = "Spam filtering system"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND LGPL-3.0-only AND MIT AND Zlib"
url = "https://rspamd.com/index.html"
source = f"https://github.com/rspamd/rspamd/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "da24e8b85d201c4670f1f280d4a0ba29733c88b1e9a021fd85eace9c5861a5a9"


match self.profile().arch:
    case "aarch64" | "ppc64le" | "x86_64":
        configure_args += ["-DENABLE_HYPERSCAN=ON"]
        makedepends += ["vectorscan-devel"]


def do_check(self):
    # full tests require luajit
    self.do("build/test/rspamd-test-cxx")


def post_install(self):
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="rspamd.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="rspamd.conf",
    )
    self.install_service(self.files_path / "rspamd")
    self.install_license("LICENSE.md")