import unittest

from main import Solution

class test(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    def test1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,2,3,5,6])    
# [7,8,9,0,0,0]
# [2,5,6]
    def test2(self):
        num1 = [7,8,9,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
if __name__ == "__main__":
    unittest.main()