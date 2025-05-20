import unittest
from typing import List, Dict
from main import Solution
class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        points = [[1,3],[-2,2]]
        k = 1
        ans = [[-2,2]]
        res = self.ins.kClosest(points=points,k=k)
        self.assertEqual(ans,res)

    def test2(self):
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        ans = [[3,3],[-2,4]]
        res = self.ins.kClosest(points=points,k=k)
        self.assertEqual(ans,res)

    def test3(self):
        points = [[-5,4],[-6,-5],[4,6]]
        k = 2
        ans = [[-5,4],[4,6]]
        res = self.ins.kClosest(points=points,k=k)
        self.assertEqual(ans,res)

    # def testdict(self):
    #     points = [[3,3],[5,-1],[-2,4]]
    #     res: dict[int:List[int]] = self.ins.makedict(points=points)
    #     ans = {4:[0,2],5:[1]}
    #     self.assertEqual(res,ans)
        
    # def test_cal1(self):
    #     point = [3,3]
    #     res = self.ins.calculateDisSquare(3,3)
    #     ans = 4
    #     self.assertEqual(res,ans)
    
    # def test_cal2(self):
    #     point = [-2,4]
    #     res = self.ins.calculateDisSquare(point[0],point[1])
    #     ans = 4
    #     self.assertEqual(res,ans)

if __name__=="__main__":
    unittest.main()