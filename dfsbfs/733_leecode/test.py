import unittest
from main2 import Solution

from typing import List

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    

    def test1(self):
        image = [[1,1,1],
                 [1,1,0],
                 [1,0,1]]
        color: int = 2
        sr, sc = 1, 1
        ans = [[2,2,2],
               [2,2,0],
               [2,0,1]]
        res = self.instance.floodFill(image, sr, sc, color)
        self.assertEqual(res, ans)

    def test2(self):
        image = [[0,0,0],
                 [0,0,0]]
        color: int = 0
        sr, sc = 0, 0
        ans = [[0,0,0],
               [0,0,0]]
        res = self.instance.floodFill(image, sr, sc, color)
        self.assertEqual(res, ans)

    def test3(self):
        image = [[0,0,0],
                 [0,0,0]]
        color: int = 2
        sr, sc = 1, 0
        ans = [[2,2,2],
               [2,2,2]]
        res = self.instance.floodFill(image, sr, sc, color)
        self.assertEqual(res, ans)

    
    def test4(self):
        image = [[0,0,0],
                 [0,0,1]]
        color: int = 2
        sr, sc = 1, 0
        ans = [[2,2,2],
               [2,2,1]]
        res = self.instance.floodFill(image, sr, sc, color)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()

