pkgname = "textadept"
pkgver = "12.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DNIGHTLY=0",
    "-DQT=1",
    "-DGTK3=0",
    "-DGTK2=0",
    "-DCURSES=0",
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DCMAKE_BUILD_TYPE=None",
]
make_cmd = "ninja"
make_dir = "build_dir"
make_install_args = ["-v"]
hostmakedepends = ["cmake", "pkgconf", "ninja", "tree"]
makedepends = [
    "qt6-qt5compat",
    "qt6-qt5compat-devel",
]
pkgdesc = "Fast, minimalist, and remarkably extensible cross-platform text editor"
maintainer = "fsx <frank@61924.nl>"
license = "MIT"
url = "https://orbitalquark.github.io/textadept"
source = [
    "https://github.com/orbitalquark/textadept/archive/refs/tags/textadept_12.2.tar.gz",
    "!https://www.scintilla.org/scintilla537.tgz",
    "!https://www.scintilla.org/lexilla510.tgz",
    "!https://github.com/orbitalquark/scinterm/archive/scinterm_5.0.zip",
    "!https://github.com/orbitalquark/scintillua/archive/48a6fc9511ec67993e43ac7f5a33efc616b7ea32.zip",
    "!https://www.lua.org/ftp/lua-5.4.6.tar.gz",
    "!https://github.com/roberto-ieru/LPeg/archive/e58f9bb289b1aa5cd4c96c26cccd0f69461e8436.zip>lpeg-1.1.0.tar.gz",
    "!https://github.com/lunarmodules/luafilesystem/archive/refs/tags/v1_8_0.zip",
    "!https://github.com/orbitalquark/lua-std-regex/archive/1.0.zip",
    "!https://github.com/ThomasDickey/cdk-snapshots/archive/refs/tags/t20200923.tar.gz",
    "!https://www.leonerd.org.uk/code/libtermkey/libtermkey-0.22.tar.gz",
    "!https://github.com/itay-grudev/SingleApplication/archive/refs/tags/v3.4.0.zip",
]
source_paths = [
    ".",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
    "build_dir/_deps/",
]
sha256 = [
    "1e5b6eca26dbdb06b8aca1c1f743a28674c2205bf8870a1e6f3a2da9f57f4071",
    "e75120a74e3266eb50b07c91e14503d736a716958361b20751d7de9ee03c1954",
    "6b3595274005498671b854cf57bdeec2254966f371712fcf3a716d97aa7f3fd8",
    "975a9e2cc0ab872a1903f19f997151db4ad8e44b14a0ee5efb5bd926d61d6f6e",
    "a26e00c03680220fa23ed791e5bb7d8a79c7e35062e54ff5d16d14cc90558bf6",
    "7d5ea1b9cb6aa0b59ca3dde1c6adcb57ef83a1ba8e5432c0ecd06bf439b3ad88",
    "8041da6c8905e6a194c04c7bb8c26c255be7befd2bc653e2fab746a1b202b3c8",
    "e3a6beca7a8a90522eed31db6ccdc5ed65a433826500c6862784e27671b9e18a",
    "5b684a1ce7ea632a37aa4f98bcf265cd97d9d70c5998c56985295c6aa97e74e1",
    "ae32f8a0c483259580649f291bc140a5fa6fad5349bd8fba0fc655fa0c2f0e72",
    "6945bd3c4aaa83da83d80a045c5563da4edd7d0374c62c0d35aec09eb3014600",
    "170cb333e47d00ba461fdbb645769be12aa2e10fa9dd0b3ef0475f8633c67176",
]
# textadept has no tests.
options = ["!check"]

def post_prepare(self):
    self.mkdir("build_dir")
    self.mkdir("build_dir/_deps")
    deps_dir = "build_dir/_deps/"
    self.cp(self.sources_path / "scintilla537.tgz", deps_dir)
    self.cp(self.sources_path / "lexilla510.tgz", deps_dir)
    self.cp(self.sources_path / "scinterm_5.0.zip", deps_dir)
    self.cp(self.sources_path / "48a6fc9511ec67993e43ac7f5a33efc616b7ea32.zip", deps_dir)
    self.cp(self.sources_path / "lua-5.4.6.tar.gz", deps_dir)
    self.cp(self.sources_path / "lpeg-1.1.0.tar.gz", deps_dir)
    self.cp(self.sources_path / "v1_8_0.zip", deps_dir)
    self.cp(self.sources_path / "1.0.zip", deps_dir)
    self.cp(self.sources_path / "t20200923.tar.gz", deps_dir)
    self.cp(self.sources_path / "libtermkey-0.22.tar.gz", deps_dir)
    self.cp(self.sources_path / "v3.4.0.zip", deps_dir)


def pre_install(self):
    self.install_dir("usr/bin")
    self.install_dir("usr/share/applications")


def post_install(self):
    self.install_license("LICENSE")
    self.rm(self.destdir / "usr/bin/textadept")
    self.mv(self.destdir / "usr/share/textadept/textadept", self.destdir / "usr/bin/textadept")
