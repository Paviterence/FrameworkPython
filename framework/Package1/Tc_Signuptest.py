import unittest


class Signuptest(unittest.TestCase):
    def test_SignupbyEmail(self):
        print("this is my Signup emailtest")
        self.assertTrue(True)

    def test_SignupFacebook(self):
        print("this is my Facebook Signup test")
        self.assertTrue(True)

    def test_Signupbytwitter(self):
        print("this is my Twitter Signup test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()