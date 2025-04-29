import unittest
from main import Solution
from main_2 import Solution as s2
from typing import List

class test(unittest.TestCase):
    def setUp(self):
        self.instance = s2()
    

    def test1(self):
        target: int = 9
        nums: List[int] = [2,7,11,15]
        ans: List[int] = self.instance.twoSum(nums, target)
        self.assertEqual(ans, [1,2])

    def test2(self):
        target: int = 6
        nums: List[int] = [2,3,4]
        ans: List[int] = self.instance.twoSum(nums, target)
        self.assertEqual(ans, [1,3])

    def test3(self):
        target: int = -1
        nums: List[int] = [-1,0]
        ans: List[int] = self.instance.twoSum(nums, target)
        self.assertEqual(ans, [1,2])
    
    def test4(self):
        target: int = 8
        nums: List[int] = [1,2,4,5,6]
        ans: List[int] = self.instance.twoSum(nums, target)
        self.assertEqual(ans, [2,5])

    def test5(self):
        target: int = -8
        nums: List[int] = [-5,-4,-3,0,1,2,3]
        ans: List[int] = self.instance.twoSum(nums, target)
        self.assertEqual(ans, [1,3])
    
    def test6(self):
        target: int = 8
        nums: List[int] = [1,2,3,4,4,19,10,90]
        ans: List[int] = self.instance.twoSum(nums, target)
        self.assertEqual(ans, [4,5])
        


if __name__ == "__main__":
    unittest.main()