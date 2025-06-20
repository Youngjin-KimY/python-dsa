import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()
    
    def test1(self) -> None:
        dividened = 10
        divisor = 3
        ans = 3
        res = self.ins.divide(dividened, divisor)
        self.assertEqual(ans,res)

    def test2(self) -> None:
        dividened = -10
        divisor = 3
        ans = -3
        res = self.ins.divide(dividened, divisor)
        self.assertEqual(ans,res)        

    def test3(self) -> None:
        dividened = -7
        divisor = 3
        ans = -2
        res = self.ins.divide(dividened, divisor)
        self.assertEqual(ans,res)        
    
    def test4(self) -> None:
        dividened = 2
        divisor = 2
        ans = 1
        res = self.ins.divide(dividened, divisor)
        self.assertEqual(ans,res)

    def test5(self) -> None:
        dividened = -2147483648
        divisor = -1
        ans = 2147483647
        res = self.ins.divide(dividened, divisor)
        self.assertEqual(ans,res)

    # def test6(self) -> None:
    #     dividened = 2147483647
    #     divisor = 2
    #     ans = 1073741823
    #     res = self.ins.divide(dividened, divisor)
    #     self.assertEqual(ans,res)

    def test7(self) -> None:
        dividened = 2147483647
        divisor = 3
        ans = 715827882
        res = self.ins.divide(dividened, divisor)
        self.assertEqual(ans,res)

if __name__ == "__main__":
    unittest.main()