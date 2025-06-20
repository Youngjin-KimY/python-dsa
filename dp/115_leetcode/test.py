import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()

    def test1(self) -> None:
        s = "rabbbit"
        t = "rabbit"
        ans = 3
        res = self.ins.numDistinct(s,t) 
        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()

