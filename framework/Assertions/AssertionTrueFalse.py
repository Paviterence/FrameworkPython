import unittest
#assertion true or False
from selenium import webdriver
class SearchEngineTest(unittest.TestCase):
    @classmethod #decorator
    def setUp(self) :
        self.driver = webdriver.Chrome()
        print("setup executed")
    @classmethod
    def tearDown(self):
        self.driver.close()
        print("teardown done")

    def test_Google(self):
        self.driver.get("https://www.google.com/")
        Titleofthepage = self.driver.title
        self.assertTrue(Titleofthepage=="Google","tittle not matching test cases failed")
        print("google test is done")

    def test_Bing(self):
        self.driver.get("https://www.bing.com/")
        Titleofthepage=self.driver.title
        self.assertFalse(Titleofthepage=="Google","TEST PASSED BECAUSE BOTH TITLE ARE DIFFERENT")
        print("bingo test is passed")


if __name__=="__main__":
    unittest.main()