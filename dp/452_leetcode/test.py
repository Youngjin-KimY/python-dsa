import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()

    def test_case_1(self):
        t = [[10,16],[2,8],[1,6],[7,12]]
        ans = 2
        res = self.ins.findMinArrowShots(t)
        self.assertEqual(ans, res)

    def test_case_2(self):
        t = [[1,2],[3,4],[5,6],[7,8]]
        ans = 4
        res = self.ins.findMinArrowShots(t)
        self.assertEqual(ans, res)

    def test_case_3(self):
        t = [[1,2],[2,3],[3,4],[4,5]]
        ans = 2
        res = self.ins.findMinArrowShots(t)
        self.assertEqual(ans, res)

    def test_case_4(self):
        t = [[2,3],[2,3]]
        ans = 1
        res = self.ins.findMinArrowShots(t)
        self.assertEqual(ans, res)
if __name__ == "__main__":
    unittest.main()