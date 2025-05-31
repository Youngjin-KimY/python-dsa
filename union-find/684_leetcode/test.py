import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()

    def test1(self) -> None:
        edges = [[1,2],[1,3],[2,3]]
        ans = [2,3]
        res = self.ins.findRedundantConnection(edges=edges)
        self.assertEqual(ans,res)

    def test2(self) -> None:
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        ans = [1,4]
        res = self.ins.findRedundantConnection(edges=edges)
        self.assertEqual(ans,res)

    def test3(self) -> None:
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5], [4,5]]
        ans = [4,5]
        res = self.ins.findRedundantConnection(edges=edges)
        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()