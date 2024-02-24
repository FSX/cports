pkgname = "python-black"
pkgver = "24.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
depends = [
    "python-click",
    "python-mypy_extensions",
    "python-packaging",
    "python-pathspec",
    "python-platformdirs",
]
checkdepends = [
    "python-aiohttp",
    "python-ipython",
    "python-pytest",
    "python-pytest-xdist",
    "python-tokenize_rt",
] + depends
pkgdesc = "Python formatting tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://black.readthedocs.io"
source = f"$(PYPI_SITE)/b/black/black-{pkgver}.tar.gz"
sha256 = "bce4f25c27c3435e4dace4815bcb2008b87e167e3bf4ee47ccdc5ce906eb4894"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
