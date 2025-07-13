import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        n = [4,2,3]
        k = 1
        res = self.test_instance.largestSumAfterKNegations(n,k)
        ans = 5
        self.assertEqual(res, ans)

    def test2(self):
        n = [3,-1,0,2] 
        k = 3
        res = self.test_instance.largestSumAfterKNegations(n,k)
        ans = 6
        self.assertEqual(res, ans)

    def test3(self):
        n = [2,-3,-1,5,-4]
        k = 2
        res = self.test_instance.largestSumAfterKNegations(n,k)
        ans = 13
        self.assertEqual(res, ans)
    
    def test4(self):
        n = [-2, 8,4,9,9]
        k = 5
        res = self.test_instance.largestSumAfterKNegations(n,k)
        ans = 32
        self.assertEqual(res, ans)

if __name__ == "__main__":
    unittest.main()