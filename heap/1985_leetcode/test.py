import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        
        self.ins = Solution()

    def test1(self) -> None:
        t1 = ["3","6","7","10"]
        k = 4
        ans = "3"
        res = self.ins.kthLargestNumber(t1,k)
        self.assertEqual(ans,res)

    def test2(self) -> None:
        t1 = ["0","0"]
        k = 2
        ans = "0"
        res = self.ins.kthLargestNumber(t1,k)
        self.assertEqual(ans,res)


if __name__ == "__main__":
    unittest.main()