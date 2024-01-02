pkgname = "nng"
pkgver = "1.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DNNG_ENABLE_TLS=ON",
    "-DBUILD_SHARED_LIBS=ON",
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
source = "https://github.com/nanomsg/nng/archive/refs/tags/v1.7.0.tar.gz"
sha256 = "668325161637a0debcf7fb4340919b81e74b66d38bc7a663e8b55b7e0abd7f57"
# Some tests need internet.
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
