import unittest

from main import Solution

class test(unittest.TestCase):

    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        nums = [1,2,5,2,3]
        target = 2        
        ans = self.test_instance.targetIndices(nums, target)
        self.assertEqual(ans, [1,2])
    def test3(self):
        nums = [1,2,5,2,3]
        target = 3
        ans = self.test_instance.targetIndices(nums, target)
        self.assertEqual(ans, [3])
# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:
    def test2(self):
        nums = [1,2,5,2,3]
        target = 5
        ans = self.test_instance.targetIndices(nums, target)
        self.assertEqual(ans, [4])
# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
if __name__ == "__main__":
    unittest.main()