import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        tlis = [2,2,3,7]
        tel = 7
        r = self.ins.combinationSum(tlis, tel)
        ans = [[2,2,3],[7]]
        self.assertEqual(r,ans)

    def test2(self):
        tlis = [2,3,6,7]
        tel = 7
        r = self.ins.combinationSum(tlis, tel)
        ans = [[7]]
        self.assertEqual(r,ans)
    

if __name__ == "__main__":
    unittest.main()