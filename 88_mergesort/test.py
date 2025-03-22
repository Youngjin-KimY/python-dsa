import unittest
from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.test = Solution()
    
    def test1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        self.test.merge(nums1,m,nums2,n)
        ans = nums1
        self.assertEqual(ans, [1,2,3,0,0,0])

if __name__ == "__main__":
    unittest.main()
