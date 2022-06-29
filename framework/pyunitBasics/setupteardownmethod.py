import unittest
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
        print("Title of the page",self.driver.title)
    def test_Bing(self):
        self.driver.get("https://www.bing.com/")
        print("Title of the page",self.driver.title)

if __name__=="__main__":
    unittest.main()