import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()
    
    def test1(self):
        arr= [1,2,3,4,5]
        k = 4
        x = 3
        ans = [1, 2, 3, 4]
        res = self.ins.findClosestElements(arr=arr, k=k,x=x)
        self.assertEqual(ans,res)

    def test2(self):
        arr= [1,1,2,3,4,5]
        k = 4
        x = -1
        ans = [1, 1, 2, 3]
        res = self.ins.findClosestElements(arr=arr, k=k,x=x)
        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()