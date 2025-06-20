import unittest

from main import Solution
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()
    
    def test1(self):
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        res = self.ins.minimumTotal(triangle=triangle)
        ans = 11

        self.assertEqual(res,ans)


    def test2(self):
        tri = [[-10]]
        res = self.ins.minimumTotal(tri)
        ans = -10
        self.assertEqual(ans,res)


if __name__ == "__main__":
    unittest.main()