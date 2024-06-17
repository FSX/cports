pkgname = "libharu"
pkgver = "2.4.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "libpng-devel",
    "zlib-devel",
]
pkgdesc = "C library for generating pdfs"
maintainer = "psykose <alice@ayaya.dev>"
license = "Zlib"
url = "https://github.com/libharu/libharu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "227ab0ae62979ad65c27a9bc36d85aa77794db3375a0a30af18acdf4d871aee6"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libharu-devel")
def _devel(self):
    return self.default_devel()
