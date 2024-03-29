pkgname = "graphicsmagick"
pkgver = "1.3.43"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-shared",
    "--with-bzlib",
    "--with-gs-font-dir=/usr/share/fonts/Type1",
    "--with-jbig",
    "--with-jp2",
    "--with-jxl",
    "--with-heif",
    "--with-lcms2",
    "--with-lzma",
    "--with-modules",
    "--with-perl",
    "--with-png",
    "--with-quantum-depth=16",
    "--with-threads",
    "--with-tiff",
    "--with-ttf",
    "--with-webp",
    "--with-x",
    "--with-zlib",
    "--with-zstd",
]
hostmakedepends = ["automake", "libtool", "perl", "pkgconf"]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "jasper-devel",
    "jbigkit-devel",
    "lcms2-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libltdl-devel",
    "libomp-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxml2-devel",
    "xz-devel",
    "zstd-devel",
]
pkgdesc = "Image processing system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.graphicsmagick.org"
source = f"$(SOURCEFORGE_SITE)/graphicsmagick/GraphicsMagick-{pkgver}.tar.xz"
sha256 = "2b88580732cd7e409d9e22c6116238bef4ae06fcda11451bf33d259f9cbf399f"


def post_install(self):
    self.install_license("Copyright.txt")


@subpackage("graphicsmagick-devel")
def _devel(self):
    return self.default_devel()
