import unittest
from leetcode_2 import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    
    def test1(self):
        input: str = "abcabcbb"
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 3)
    
    def test2(self):
        input: str = "bbbbb"
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 1)

    def test3(self):
        input: str = "pwwkew"
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 3)
    
    def test4(self):
        input: str = "aab"
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 2)
    
    def test5(self):
        input: str = "dvda"
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 3)
    
    def test6(self):
        input: str = " "
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 1)

    def test7(self):
        input: str = "tmmzuxt"
        ans = self.instance.lengthOfLongestSubstring(input)
        self.assertEqual(ans, 5)

if __name__ == "__main__":
    unittest.main()
