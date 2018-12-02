from drozer.modules import Module

class GetUidFromPackage(Module) :
    name = "Get a package name from the given UID"
    description = "Get a package's name from the given UID"
    examples = """
dz> run app.package.getpackagefromuid com.mwr.dz
com.mwr.dz:2000
"""

    author = "Tyrone"
    date = "2018-12-02"
    license = "BSD (3 clause)"
    path = ["app", "package"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]
    
    def add_arguments(self, parser) :
        parser.add_argument("pkg", help="package name")
        
    def execute(self, arguments) :
        context = self.getContext()
        pm = context.getPackageManager()
        name = pm.getPackageUid(arguments.pkg ,0 )
        self.stdout.write("Package %s is %s\n\n" % (arguments.pkg, name))

