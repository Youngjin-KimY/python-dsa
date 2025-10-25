import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        t = 4
        r = self.ins.solveNQueens(t)
        ans = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        self.assertEqual(r, ans)

    # def test2(self):
    #     t = 2
    #     r = self.ins.solveNQueens(t)
    #     ans = []
    #     self.assertEqual(r,ans)
    # def test3(self):
    #     t = 3
    #     r = self.ins.solveNQueens(t)
    #     ans = []
    #     self.assertEqual(r,ans)

    def test4(self):
        t = 1
        r = self.ins.solveNQueens(t)
        ans = [["Q"]]
        self.assertEqual(r,ans)

if __name__ == "__main__":
    unittest.main()