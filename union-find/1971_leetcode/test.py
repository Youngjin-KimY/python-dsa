import unittest

from main import Solution
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()

    def test1(self) -> None:
        n = 3
        edges = [[0,1],[1,2],[2,0]]
        source = 0
        destinaton = 2
        ans = True
        res = self.ins.validPath(n,edges,source, destinaton)
        self.assertEqual(ans,res)

    def test2(self) -> None:
        n = 6
        edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
        source = 0
        destinaton = 5
        ans = False
        res = self.ins.validPath(n,edges,source, destinaton)
        self.assertEqual(ans,res)        

    def test3(self) -> None:
        n = 10
        edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
        source = 7
        destinaton = 5
        ans = True
        res = self.ins.validPath(n,edges,source, destinaton)
        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()