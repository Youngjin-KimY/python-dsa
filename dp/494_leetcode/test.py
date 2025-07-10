import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.ins = Solution()
    

    def test1(self) -> None:
        nums = [1,1,1,1,1]
        t = 3
        ans = 5
        res = self.ins.findTargetSumWays(nums=nums, target=t)
        self.assertEqual(ans,res)
    
    def test2(self) -> None:
        nums = [1]
        t = 1
        ans = 1
        res = self.ins.findTargetSumWays(nums=nums, target=t)
        self.assertEqual(ans,res)

    def test3(self) -> None:
        nums = [1]
        t = 2
        ans = 0
        res = self.ins.findTargetSumWays(nums=nums, target=t)
        self.assertEqual(ans,res)

    def test4(self) -> None:
        nums = [1,0]
        t = 1
        ans = 2
        res = self.ins.findTargetSumWays(nums=nums, target=t)
        self.assertEqual(ans,res)
    


if __name__ == "__main__":
    unittest.main()