import unittest

from main import Solution

class test(unittest.TestCase):

    # def __init__(self, methodName = "runTest"):
    #     super().__init__(methodName)
    #     self.test_instance = Solution()

    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        nums = [2,1,3,3]
        k = 2        
        ans = self.test_instance.maxSubsequence(nums, k)
        self.assertEqual(ans, [3,3])

    def test2(self):
        nums = [-1,-2,3,4]
        k = 3        
        ans = self.test_instance.maxSubsequence(nums, k)
        self.assertEqual(ans, [-1,3,4])


    def test3(self):
        nums = [3,4,3,3]
        k = 2        
        ans = self.test_instance.maxSubsequence(nums, k)
        self.assertEqual(ans, [3,4])

    def test4(self):
        nums = [50, -75]
        k = 2        
        ans = self.test_instance.maxSubsequence(nums, k)
        self.assertEqual(ans, [50, -75])

if __name__ == "__main__":
    unittest.main()