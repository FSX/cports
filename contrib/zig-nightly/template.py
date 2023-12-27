pkgname = "zig-nightly"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DZIG_PIE=ON",
    "-DZIG_SHARED_LLVM=ON",
    "-DZIG_TARGET_MCPU=baseline",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "clang-devel",
    "linux-headers",
    "lld-devel",
    "llvm-devel",
    "ncurses-devel",
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Zig programming language toolchain"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ziglang/zig"
source = f"https://ziglang.org/builds/zig-{pkgver}-dev.1767+1e42a3de8.tar.xz"
sha256 = "79287ee481ae844aa4fe38e22f7e8dcf1a7f5f0812f105a80a21c62b89b44dcc"
# lighten up the build, only applies to bootstrap
hardening = ["!int", "!scp", "!var-init"]
# lto only gets applied to the C bootstrap and slows down the build (doesn't
# affect the zig output)
options = ["!lto"]

# ditto
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE", "-Wno-incompatible-pointer-types"]}

match self.profile().arch:
    case "x86_64" | "aarch64":
        pass
    case _:
        # disable tests on other archs, a lot of them fail
        options += ["!check"]


def do_check(self):
    self.do(
        self.make_dir + "/stage3/bin/zig",
        "build",
        "test",
        "--summary",
        "all",
        "-Dcpu=baseline",
        "-Dskip-cross-glibc",
        "-Dskip-debug",
        "-Dskip-non-native",
        "-Dskip-release-safe",
        "-Dskip-release-small",
    )


def post_install(self):
    self.install_license("LICENSE")
