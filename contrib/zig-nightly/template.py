pkgname = "zig-nightly"
pkgver = "0.12.0"
pkgrel = 3
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
source = "https://ziglang.org/builds/zig-0.12.0-dev.1856+94c63f31f.tar.xz"
sha256 = "9045bfc9da86a3e13f6a5c2793e992093b1089756deeddc1a03fadd221fc4148"
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
