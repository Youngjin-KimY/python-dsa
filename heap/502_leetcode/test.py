import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    def test1(self):
        k = 2
        w = 0
        profits = [1,2,3]
        capital = [0,1,1]
        res = self.ins.findMaximizedCapital(k,w,profits,capital)
        ans = 4
        self.assertEqual(res,ans)

    def test2(self):
        k = 3
        w = 0
        profits = [1,2,3]
        capital = [0,1,2]
        res = self.ins.findMaximizedCapital(k,w,profits,capital)
        ans = 6
        self.assertEqual(res,ans)

    def test3(self):
        k = 1
        w = 0
        profits = [1,2,3]
        capital = [1,1,2]
        res = self.ins.findMaximizedCapital(k,w,profits,capital)
        ans = 0
        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()