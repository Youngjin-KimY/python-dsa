import unittest

from typing import List
from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()


    def test1(self):
        arr = [1,1,1,2,2,3]
        k = 2
        ans = [1,2]
        res = self.ins.topKFrequent(arr, k)
        self.assertEqual(ans, res)

    def test2(self):
        arr = [1]
        k = 1
        ans = [1]
        res = self.ins.topKFrequent(arr, k)
        self.assertEqual(ans, res)
    
    def test3(self):
        arr = [-1, -1]
        k = 1
        ans = [-1]
        res = self.ins.topKFrequent(arr, k)
        self.assertEqual(ans, res)

    def test5(self):
        arr = [3,0,1,0]
        k = 1
        ans = [0]
        res = self.ins.topKFrequent(arr, k)
        self.assertEqual(ans, res)

if __name__ == "__main__":
    unittest.main()