pkgname = "font-manager"
pkgver = "0.8.8"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dnautilus=true",
    "-Dthunar=true",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
    "yelp-tools",
]
makedepends = [
    "gtk+3-devel",
    "json-glib-devel",
    "libsoup-devel",
    "nautilus-devel",
    "thunar-devel",
    "webkitgtk-devel",
]
pkgdesc = "Font management application"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://fontmanager.github.io"
source = f"https://github.com/FontManager/font-manager/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7badeefe47df3f21d4e9087889fe3d2a6f8e97c95c32fa7fae78ccb59ac40868"
# gobject-introspection
options = ["!cross"]


@subpackage("font-manager-nautilus")
def _nautilus(self):
    self.pkgdesc = f"{pkgdesc} (nautilus plugin)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "nautilus"]
    return ["usr/lib/nautilus"]


@subpackage("font-manager-thunar")
def _thunar(self):
    self.pkgdesc = f"{pkgdesc} (thunar plugin)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "thunar"]
    return ["usr/lib/thunarx-3"]
