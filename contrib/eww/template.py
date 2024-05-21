pkgname = "eww"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "gtk-layer-shell-devel",
    "libdbusmenu-devel",
    "rust-std",
]
pkgdesc = "Standalone widget system for wayland written in rust"
maintainer = "Nova <froggo8311@proton.me>"
license = "MIT"
url = "https://elkowar.github.io/eww"
source = f"https://github.com/elkowar/eww/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cef361946946c566b79f8ddc6208d1a3f16b4ff9961439a3f86935e1cfa174a1"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"eww.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/eww",
                "shell-completions",
                "--shell",
                shell,
                stdout=f,
            )


def do_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"eww.{shell}", shell)
    self.install_bin(f"./target/{self.profile().triplet}/release/eww")
    self.install_license("LICENSE")
