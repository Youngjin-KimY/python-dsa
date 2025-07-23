import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        t = [[1,2],[2,3],[3,4],[1,3]]
        res=self.test_instance.eraseOverlapIntervals(t)
        ans = 1
        self.assertEqual(res,ans)
        

    def test2(self):
        t = [[1,2],[1,2],[1,2]]
        res=self.test_instance.eraseOverlapIntervals(t)
        ans = 2
        self.assertEqual(res,ans)

    def test3(self):
        t = [[1,2],[2,3]]
        res=self.test_instance.eraseOverlapIntervals(t)
        ans = 0
        self.assertEqual(res,ans)

    def test4(self):
        t = [[1,100],[11,22],[1,11],[2,12]]
        # 1,11 / 2,12 / 11,22/ 1,100
        res=self.test_instance.eraseOverlapIntervals(t)
        ans = 2
        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()