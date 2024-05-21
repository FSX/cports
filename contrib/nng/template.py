pkgname = "nng"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DNNG_ENABLE_TLS=OFF",
    "-DBUILD_SHARED_LIBS=ON",
    "-DNNG_ENABLE_COMPAT=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "mbedtls-devel",
]
depends = ["mbedtls"]
pkgdesc = "High-Performance Scalability Protocols NextGen"
maintainer = "fsx <frank@61924.nl>"
license = "MIT"
url = "https://nng.nanomsg.org"
source = "https://github.com/nanomsg/nng/archive/refs/tags/v1.8.0.tar.gz"
sha256 = "cfacfdfa35c1618a28bb940e71f774a513dcb91292999696b4346ad8bfb5baff"
# Some tests need internet.
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
