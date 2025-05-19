import unittest
from main import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()

    def test1(self):
        # Input: temperatures = [73,74,75,71,69,72,76,73]
        # Output: [1,1,4,2,1,1,0,0]
        tem = [73,74,75,71,69,72,76,73]
        ans = [1,1,4,2,1,1,0,0]
        res = self.ins.dailyTemperatures(tem)
        self.assertEqual(res, ans)
    
    def test2(self):
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
        tem = [30,40,50,60]
        ans = [1,1,1,0]
        res = self.ins.dailyTemperatures(temperatures=tem)
        self.assertEqual(res,ans)

    def test3(self):
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
        tem = [30,60,90]
        ans = [1,1,0]
        res = self.ins.dailyTemperatures(temperatures=tem)
        self.assertEqual(res,ans)

    def test4(self):
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
        tem = [10,9,8,7,5]
        ans = [0,0,0,0,0]
        res = self.ins.dailyTemperatures(temperatures=tem)
        self.assertEqual(res,ans)

    def test5(self):
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
        tem = [1,1,1,1,1]
        ans = [0,0,0,0,0]
        res = self.ins.dailyTemperatures(temperatures=tem)
        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()