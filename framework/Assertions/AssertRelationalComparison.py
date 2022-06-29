import unittest
class AssertRelation(unittest.TestCase):
    def test_Assert(self):
        # self.assertGreater(20,10,"test passed")#1 st one is compared with second one
        # self.assertGreaterEqual(30,30)
        # self.assertLess(5,10)
        self.assertLessEqual(3,3)

if __name__ == "--main--":
    unittest.main()