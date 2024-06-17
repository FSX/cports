pkgname = "wireplumber"
pkgver = "0.5.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystem-lua=true",
    "-Ddoc=disabled",
    "-Dintrospection=enabled",
]
hostmakedepends = [
    "doxygen",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-lxml",
]
makedepends = ["pipewire-devel", "glib-devel", "lua5.4-devel"]
checkdepends = ["pipewire", "dbus"]
depends = ["pipewire"]
provides = [f"pipewire-session-manager={pkgver}-r{pkgrel}"]
pkgdesc = "Session and policy manager implementation for PipeWire"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "626cfaf090efb5359454a30c9b288e068ea04289b341dc4d5c7064fd6b1427b4"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user", enable=True)


@subpackage("wireplumber-devel")
def _devel(self):
    return self.default_devel()
