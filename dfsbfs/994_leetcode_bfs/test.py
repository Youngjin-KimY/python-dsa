import unittest
from main import Solution, Point
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from node import TreeNode

from typing import List
from collections import deque

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def testStartPoint(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        res: List[Point] = self.instance.findRottenPointList(grid)
        expect = [Point(0,0)]
        self.assertEqual(expect[0], res[0])

    def testStartPoint2(self):
        grid = [[1,1,1],[1,2,0],[0,1,1]]
        res: List[Point] = self.instance.findRottenPointList(grid)
        expect = [Point(1,1)]
        self.assertEqual(expect[0], res[0])
        self.assertEqual(expect[0], res[0])

    def testStartPoint3(self):
        grid = [[1,1,1],[1,2,0],[0,1,2]]
        res: List[Point] = self.instance.findRottenPointList(grid)
        expect = [Point(1,1), Point(2,2)]
        self.assertEqual(expect[0], res[0])
        self.assertEqual(expect[1], res[1])        

    def test1(self):
        grid = [[2,1,1],
                [1,1,0],
                [0,1,1]]
        res = self.instance.orangesRotting(grid)
        expect: int = 4
        self.assertEqual(res, expect)
    
    def test2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        res = self.instance.orangesRotting(grid)
        expect: int = -1
        self.assertEqual(res, expect)

    def test3(self):
        grid = [[0,2]]
        res = self.instance.orangesRotting(grid)
        expect: int = 0
        self.assertEqual(res, expect)

    def test4(self):
        grid = [[0]]
        res = self.instance.orangesRotting(grid)
        expect: int = 0
        self.assertEqual(res, expect)
    
    def test5(self):
        grid = [[2,1,1],
                [1,1,1],
                [0,1,2]]
        res = self.instance.orangesRotting(grid)
        expect: int = 2
        self.assertEqual(res, expect)

if __name__ == "__main__":
    unittest.main()

