import unittest

from main import Solution

class Test(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ins = Solution()

    def test1(self) -> None:
        tc = [[0,1],[1,0]]
        ans = 2
        res = self.ins.shortestPathBinaryMatrix(tc)
        self.assertEqual(ans,res)

    def test2(self) -> None:
        tc = [[0,0,0],[1,1,0],[1,1,0]]
        ans = 4
        res = self.ins.shortestPathBinaryMatrix(tc)
        self.assertEqual(ans,res)

    def test3(self) -> None:
        tc = [[1,0,0],
              [1,1,0],
              [1,1,0]]
        ans = -1
        res = self.ins.shortestPathBinaryMatrix(tc)
        self.assertEqual(ans,res)
        # [[0,0,0],[1,0,0],[1,1,0]]

    def test4(self) -> None:
        tc = [[0,0,0],
              [1,0,0],
              [1,1,0]]
        ans = 3
        res = self.ins.shortestPathBinaryMatrix(tc)
        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()