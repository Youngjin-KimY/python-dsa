import unittest

from main import Solution
from typing import List

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()

    def test1(self):
        t = [1,3,-1,-3,5,3,6,7]
        k = 3
        res: List[int] = self.ins.maxSlidingWindow(t,k)
        ans = [3,3,5,5,6,7]
        self.assertEqual(res, ans)

    def test2(self):
        t = [1]
        k = 1
        res: List[int] = self.ins.maxSlidingWindow(t,k)
        ans = [1]
        self.assertEqual(res, ans)


    def test3(self):
        t = [1,2,4,6,3]
        k = 6
        res: List[int] = self.ins.maxSlidingWindow(t,k)
        ans = [6]
        self.assertEqual(res, ans)

    def test4(self):
        t = [1,3,1,2,0,5]
        k = 3
        res = self.ins.maxSlidingWindow(t,k)
        ans = [3,3,2,5]

        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()