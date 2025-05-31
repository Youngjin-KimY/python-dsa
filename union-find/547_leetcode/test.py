import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.ins = Solution()
    
    def test1(self) -> None:
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        ans = 2
        res = self.ins.findCircleNum(isConnected)
        self.assertEqual(ans, res)

    def test2(self) -> None:
        isConnected = [[1,0,0],
                       [0,1,0],
                       [0,0,1]]
        ans = 3
        res = self.ins.findCircleNum(isConnected)
        self.assertEqual(ans, res)
    
if __name__ == "__main__":
    unittest.main()