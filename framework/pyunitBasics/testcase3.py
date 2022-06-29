import unittest
def setUpModule():
    print("setup module executed once before executing any classes or methods")
def tearDownModule():
    print("tearDownModule executed once  after everything completed in  class or methods fininshed")
class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):#execute before all test methods
        print("login started")
    @classmethod
    def tearDown(self):#execute after all test methods
        print("logout done")
    @classmethod
    def setUpClass(cls):#Execute once before start the class methods
        print("open application")
    @classmethod
    def tearDownClass(cls):#Execute once after end of  the calss methods
        print("close application")
    def test_search(self):
         print("search")
    @unittest.skip("advaced search no need for this sprint")
    def test_advanced_Search(self):
         print("aaadvanced search")
    def test_prePaid(self):
         print("prepaid")
    @unittest.SkipTest
    def test_postpaid(self):
         print("postpaid")
    @unittest.skipIf(1==1,"test feature is in enhancement so its skipped")
    def test_launch(self):
        print("browser launch")
    def test_launch2(self):
        print("browser launch 2")
    def test_launch3(self):
            print("browser launch3")

if __name__== "__main__":
    unittest.main()