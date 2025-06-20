import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()


    def test1(self) ->None:
        m = 3
        n = 7
        ans = 28
        res = self.ins.uniquePaths(m,n)
        self.assertEqual(ans,res)

    def test2(self) -> None:
        m = 3
        n = 2
        ans = 3
        res = self.ins.uniquePaths(m,n)
        self.assertEqual(res,ans)




if __name__ == "__main__":
    unittest.main()