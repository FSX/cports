pkgname = "acpi"
pkgver = "1.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "ACPI client for battery, power, and thermal readings"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/acpiclient/files/acpiclient"
source = f"$(SOURCEFORGE_SITE)/acpiclient/acpi-{pkgver}.tar.gz"
sha256 = "d7a504b61c716ae5b7e81a0c67a50a51f06c7326f197b66a4b823de076a35005"
hardening = ["vis", "cfi"]
