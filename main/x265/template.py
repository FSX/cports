pkgname = "x265"
pkgver = "3.6"
pkgrel = 0
build_wrksrc = "source"
_commit = "aa7f602f7592"
build_style = "cmake"
configure_args = ["-DENABLE_PIC=1", "-DGIT_ARCHETYPE=1"]
hostmakedepends = ["pkgconf", "cmake", "ninja"]
makedepends = ["libnuma-devel", "linux-headers"]
pkgdesc = "Open source H.265/HEVC encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://x265.org"
source = f"https://bitbucket.org/multicoreware/x265_git/get/{pkgver}.tar.gz"
sha256 = "206329b9599c78d06969a1b7b7bb939f7c99a459ab283b2e93f76854bd34ca7b"
# guilty until proven wrong
hardening = ["!int"]
# cannot be reliably tested, testing option is conditional
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        configure_args += [
            "-DENABLE_ASSEMBLY=ON",
            "-DCMAKE_ASM_NASM_FLAGS=-w-macro-params-legacy",
        ]
        hostmakedepends += ["nasm"]
    case "ppc64le":
        configure_args += ["-DENABLE_ALTIVEC=ON", "-DCPU_POWER8=ON"]
    case "ppc64" | "ppc":
        configure_args += ["-DENABLE_ALTIVEC=OFF", "-DCPU_POWER8=OFF"]
    case "aarch64":
        configure_args += ["-DENABLE_ASSEMBLY=ON"]


def do_configure(self):
    from cbuild.util import cmake

    cmake.configure(
        self,
        build_dir="build-12",
        extra_args=self.configure_args
        + [
            # doesn't work with non-byte pixel value
            "-DENABLE_ALTIVEC=OFF",
            "-DENABLE_CLI=OFF",
            "-DENABLE_SHARED=OFF",
            "-DEXPORT_C_API=OFF",
            "-DHIGH_BIT_DEPTH=ON",
            "-DMAIN12=ON",
        ],
    )
    cmake.configure(
        self,
        build_dir="build-10",
        extra_args=self.configure_args
        + [
            # doesn't work with non-byte pixel value
            "-DENABLE_ALTIVEC=OFF",
            "-DENABLE_SHARED=OFF",
            "-DENABLE_CLI=OFF",
            "-DEXPORT_C_API=OFF",
            "-DHIGH_BIT_DEPTH=ON",
            "-DMAIN12=OFF",
        ],
    )
    cmake.configure(
        self,
        build_dir="build",
        extra_args=self.configure_args
        + [
            "-DEXTRA_LIB=x265_main10.a;x265_main12.a",
            "-DEXTRA_LINK_FLAGS=-L.",
            "-DLINKED_10BIT=TRUE",
            "-DLINKED_12BIT=TRUE",
        ],
    )


def do_build(self):
    from cbuild.util import cmake

    cmake.build(self, "build-12")
    cmake.build(self, "build-10")
    with self.stamp("build-symlinks") as s:
        s.check()
        self.ln_s("../build-12/libx265.a", "build/libx265_main12.a")
        self.ln_s("../build-10/libx265.a", "build/libx265_main10.a")
    cmake.build(self, "build")


@subpackage("x265-devel")
def _devel(self):
    return self.default_devel()
