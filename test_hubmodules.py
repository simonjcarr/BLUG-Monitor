import unittest
import hubmodules


class test_hubmodules(unittest.TestCase):
    def test_listModules(self):
        
        mm = hubmodules.ManageModules()
        modlist = mm.listModules()
        print modlist
        self.assertTrue('fileexists' in modlist)



    
if __name__ == "__main__":
    unittest.main()
    
    