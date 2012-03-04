#!/usr/bin/env python
#Written by Simon Carr
#4 March 2012
from optparse import OptionParser
import sys, os, shutil, tarfile



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
            
            
    def unInstallModule(self,moduleName):
        if os.path.isdir(os.path.join("./modules",moduleName)):
            response = raw_input("Are you sure you want to uninstall module " + moduleName + "(y/n)")
            if response == "y":
                shutil.rmtree(os.path.join("./modules",moduleName), False)
                print "Module " + moduleName + " uninstalled."
            else:
                print "Uninstall canceled."
        else:
            print "Can not uninstall module that is not installed"
    
    def installModule(self,archivePath):
        tar = tarfile.open(archivePath,"r:gz")
        tar.extractall("./modules")
        moduleName = os.path.basename(archivePath)[:-7]
        if not self.moduleExists(moduleName):
            print "Module install failed."
        else:
            print "module was installed."
            self.moduleDetail(moduleName, printList=True)
        
        
        
    
    def moduleDetail(self,moduleName=None,printList=True):
        moduleConfig = []
        if not moduleName:
            for module in self.listModules(False):
                config = open(os.path.join("./modules/",module,module + ".config"))
                moduleConfig.append(config.read())
                config.close()
        else:
            if not self.moduleExists(moduleName):
                return False
            config = open(os.path.join("./modules/",moduleName,moduleName + ".config"))
            moduleConfig.append(config.read())
            config.close()
        if printList:
            for config in moduleConfig:
                print config
                print "*********************"
                
        else:
            return moduleConfig
        
    def moduleExists(self,moduleName):
        if not os.path.isdir(os.path.join("./modules",moduleName)):
            return False
        else:
            return True
             
    
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
    if options.uninstall_moduleName: mm.unInstallModule(options.uninstall_moduleName)
    if options.install_moduleName: mm.installModule(options.install_moduleName)
    