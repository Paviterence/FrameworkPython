import unittest
class Logintest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("this is my loginemailtest")
        self.assertTrue(True)
    def test_LoginFacebook(self):
        print("this is my Facebooklogintest")
        self.assertTrue(True)
    def test_Loginbytwitter(self):
        print("this is my Twitterlogintest")
        self.assertTrue(True)

if __name__== "__main__":
    unittest.main()