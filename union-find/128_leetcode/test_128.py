import unittest

from main import Solution, uff

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()

    def test_uf(self):
        nums = [0,1,2,3,4,5]
        uf = uff(nums)
        uf.union(1,2)
        uf.union(1,3)
        uf.union(0, 5)

        self.assertEqual(uf.connected(2, 3),True)
        self.assertEqual(uf.connected(0, 1), False)
        
        self.assertEqual(uf.find(10), None)
    def test1(self):
        nums = [100,4,200,1,3,2]
        res = self.ins.longestConsecutive(nums)
        ans = 4
        self.assertEqual(res,ans)

    def test2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        res = self.ins.longestConsecutive(nums)
        ans = 9
        self.assertEqual(res,ans)

    def test3(self):
        nums = [1,0,1,2]
        res = self.ins.longestConsecutive(nums)
        ans = 3
        self.assertEqual(res,ans)

if __name__ == "__main__":
    unittest.main()