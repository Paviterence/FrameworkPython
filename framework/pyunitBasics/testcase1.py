import unittest
from unittest import *

class Test(unittest.TestCase):
    def test_FirsTest(self):
        print("this is my 1st testcase using unittest in python")

if __name__=="__main__":#name is representing the current module
    unittest.main()
import unittest
class MyTest(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(1, (2-1), "Sample Subraction Test")

if __name__ == '__main__':
    unittest.main()