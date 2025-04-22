import unittest
from main import Solution

from typing import List

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    

    def test1(self):
        target: int = 7
        nums: List[int] = [2,3,1,2,4,3]
        ans: int = self.instance.minSubArrayLen(target, nums)
        self.assertEqual(ans, 2)

    
    def test2(self):
        target: int = 11
        nums: List[int] = [1,1,1,1,1,1,1,1]
        ans: int = self.instance.minSubArrayLen(target, nums)
        self.assertEqual(ans, 0)

    def test3(self):
        target: int = 4
        nums: List[int] = [1,4,4]
        ans: int = self.instance.minSubArrayLen(target, nums)
        self.assertEqual(ans, 1)

    def test4(self):
        target: int = 11
        nums: List[int] = [1,2,3,4,5]
        ans: int = self.instance.minSubArrayLen(target, nums)
        self.assertEqual(ans, 3)
    


if __name__ == "__main__":
    unittest.main()

