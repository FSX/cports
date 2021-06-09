from cbuild.util import make

def init_configure(self):
    self.make = make.Make(self)

def do_configure(self):
    self.do(
        self.chroot_build_wrksrc / self.configure_script,
        self.configure_args, build = True
    )

def do_build(self):
    self.make.build()

def do_check(self):
    pass

def do_install(self):
    self.make.install()

def use(tmpl):
    tmpl.build_style = "configure"
    tmpl.init_configure = init_configure
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
