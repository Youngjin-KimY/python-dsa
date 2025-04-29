import unittest
from main import Solution

from typing import List

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    

    def test1(self):
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
    
        res = self.instance.numIslands(grid)
        expect: int = 1
        self.assertEqual(res, expect)
    
    def test2(self):
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","1"]]
    
        res = self.instance.numIslands(grid)
        expect: int = 3
        self.assertEqual(res, expect)

    def test3(self):
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","1"],
                ["1","0","1","0","1"]]
    
        res = self.instance.numIslands(grid)
        expect: int = 4
        self.assertEqual(res, expect)

    def test4(self):
        grid = [["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"]]
    
        res = self.instance.numIslands(grid)
        expect: int = 0
        self.assertEqual(res, expect)


if __name__ == "__main__":
    unittest.main()

