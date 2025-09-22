import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        tlis = [10,1,2,7,6,1,5]
        tel = 8
        r = self.ins.combinationSum2(tlis, tel)
        ans = [[1,1,6],[1,2,5],[1,7],[2,6]]
        self.assertEqual(r,ans)

    def test2(self):
        tlis = [2,5,2,1,2]
        tel = 5
        r = self.ins.combinationSum2(tlis, tel)
        ans = [[1,2,2],[5]]
        self.assertEqual(r,ans)
    

if __name__ == "__main__":
    unittest.main()