pkgname = "gptfdisk"
pkgver = "1.0.10"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake"]
makedepends = [
    "linux-headers",
    "libuuid-devel",
    "ncurses-devel",
    "popt-devel",
]
pkgdesc = "Fdisk-like partitioning tool for GPT disks"
maintainer = "reocat <ng.ct_ml@tuta.io>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/gptfdisk"
source = f"$(SOURCEFORGE_SITE)/gptfdisk/{pkgver}/gptfdisk-{pkgver}.tar.gz"
sha256 = "2abed61bc6d2b9ec498973c0440b8b804b7a72d7144069b5a9209b2ad693a282"
hardening = ["vis", "cfi"]


def do_check(self):
    self.do(
        "sh",
        "gdisk_test.sh",
    )


def do_install(self):
    self.install_bin("cgdisk")
    self.install_bin("fixparts")
    self.install_bin("gdisk")
    self.install_bin("sgdisk")
