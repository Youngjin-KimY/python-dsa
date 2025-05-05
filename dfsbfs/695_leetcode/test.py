import unittest
from main import Solution

from typing import List

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    

    def test1(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        res = self.instance.maxAreaOfIsland(grid=grid)
        ans = 6
        self.assertEqual(res, ans)

    def test2(self):
        grid = [[0,0,0,0,0,0,0,0]]
        res = self.instance.maxAreaOfIsland(grid=grid)
        ans = 0
        self.assertEqual(res, ans)
    
    def test3(self):
        grid = [[1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,0,1,1],
                [0,0,0,1,1]]
        res = self.instance.maxAreaOfIsland(grid=grid)
        ans = 4
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()

