import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()

    def test1(self):
        t = [-1,0,1,2,-1,-4]
        ans = [[-1,-1,2],[-1,0,1]]
        res = self.ins.threeSum(t)

        self.assertEqual(ans,res)

    def test2(self):
        t = [0,0,0,0]
        ans = [[0,0,0]]
        res = self.ins.threeSum(t)

        self.assertEqual(ans,res)
    
    def test3(self):
        t = [0,0,0,]
        ans = [[0,0,0]]
        res = self.ins.threeSum(t)

        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()