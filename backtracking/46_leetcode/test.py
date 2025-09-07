import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        t = [1,2,3]
        res=self.test_instance.permute(t)
        ans = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(res,ans)

    def test2(self):
        t = [0,1]
        res=self.test_instance.permute(t)
        ans = [[0,1],[1,0]]
        self.assertEqual(res,ans)

    def test3(self):
        t = [1]
        res=self.test_instance.permute(t)
        ans = [[1]]
        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()