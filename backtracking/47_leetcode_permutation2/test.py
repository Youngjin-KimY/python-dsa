import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        t = [1,1,2]
        res=self.test_instance.permuteUnique(t)
        ans = [[1,1,2],
                [1,2,1],
                [2,1,1]]
        self.assertEqual(res,ans)

    def test2(self):
        t = [1,2,3]
        res=self.test_instance.permuteUnique(t)
        ans = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()