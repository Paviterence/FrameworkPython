#assertIn & assertnot in
import unittest
class AssertTest(unittest.TestCase):
    def test_name(self):
        list={"python","java","selenium"}
        # self.assertIn("python",list)
        self.assertNotIn("ruby", list)

if __name__== "__main__":
    unittest.main()