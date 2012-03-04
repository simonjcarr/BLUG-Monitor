#Written by Simon Carr
#4 March 2012
from optparse import OptionParser
import sys, os



class ManageModules:
    def __init__(self):
        pass
    
    def listModules(self, printList=True):
        moduleList = [x for x in os.listdir("./modules") if os.path.isdir(os.path.join("./modules",x))]
        if printList:
            for module in moduleList:
                print module
        else:
            return moduleList
            
            
    def unInstallModule(self):
        pass
    
    def installModule(self):
        pass
    
    def moduleDetail(self,moduleName=None,printList=True):
        moduleConfig = []
        if not moduleName:
            for module in self.listModules(False):
                config = open(os.path.join("./modules/",module,module + ".config"))
                moduleConfig.append(config.read())
                config.close()
        else:
            config = open(os.path.join("./modules/",moduleName,moduleName + ".config"))
            moduleConfig.append(config.read())
            config.close()
        if printList:
            for config in moduleConfig:
                print config
                print "*********************"
                
        else:
            return moduleConfig
            
    
if __name__ == "__main__":
    mm = ManageModules()
    parser = OptionParser()
    parser.add_option("-l","--list",action="store_true",dest="listModules")
    parser.add_option("-u","--uninstall",dest="uninstall_moduleName",help="Uninstall a module")
    parser.add_option("-i","--install",dest="install_moduleName",help="Installs a new module. By default the script will check GitHub for latest version of the module and download. To specify a gz archive use -a or --archive and give path to archive.")
    parser.add_option("-a","--archive",dest="archivePath",help="Use in conjunction with -i to specify the location of an archive file to install")
    parser.add_option("-d","--detail",dest="details_moduleName",default=None,help="Print details of specified module. If 'ALL' specified detail is printed for all installed modules")
    (options, args) = parser.parse_args()
    
    if options.listModules == True: mm.listModules()
    if options.details_moduleName:     
        if options.details_moduleName == "ALL":
            mm.moduleDetail()
        else:
            mm.moduleDetail(options.details_moduleName,True)