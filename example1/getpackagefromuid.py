# This is Chapter 6, pg 195
# Analysing android apps via custom module

from drozer.modules import Module

class GetPackageFromUID(Module) :
    name = "Get a package name from the given UID"
    description = "Get a package's name from the given UID"
    examples = """
dz> run app.package.getpackagefromuid 2000
android.uid.shell:2000
"""

    author = "Tyrone"
    date = "2014-05-30"
    license = "BSD (3 clause)"
    path = ["app", "package"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]
    
    def add_arguments(self, parser) :
        parser.add_argument("uid", help="uid of package")
        
    def execute(self, arguments) :
        context = self.getContext()
        pm = context.getPackageManager()
        name = pm.getNameForUid(int(arguments.uid))
        
        self.stdout.write("UID %s is %s\n\n" % (arguments.uid, name))
