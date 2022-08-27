import unittest
from selenium import webdriver
class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        driver=webdriver.Chrome()
        # driver=None
        self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__== "__main__":
    unittest.main()
