import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()

    def test_case_1(self):
        t = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        ans = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        res = self.ins.reconstructQueue(t)
        self.assertEqual(ans, res)

if __name__ == "__main__":
    unittest.main()