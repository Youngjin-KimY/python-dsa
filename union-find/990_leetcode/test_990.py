import unittest

from main import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ins = Solution()

    def testparser1(self):
        eq = "a==b"
        u,v,e = self.ins.parserEquation(eq)

        self.assertEqual(u, "a")
        self.assertEqual(v, "b")
        self.assertEqual(e, "==")
    
    def testparser2(self):
        eq = "a!=b"
        u,v,e = self.ins.parserEquation(eq)

        self.assertEqual(u, "a")
        self.assertEqual(v, "b")
        self.assertEqual(e, "!=")


    def test1(self):
        e = ["a==b","a!=b"]
        ans = False
        res = self.ins.equationsPossible(e)
        self.assertEqual(ans,res)

    def test2(self):
        e = ["a==b","a==b"]
        ans = True
        res = self.ins.equationsPossible(e)
        self.assertEqual(ans,res)

    def test3(self):
        e = ["c==c","b==d","x!=z"]
        ans = True
        res = self.ins.equationsPossible(e)
        self.assertEqual(ans,res)

    def test5(self):
        e = ["a==b","b!=c","c==a"]
        ans = False
        res = self.ins.equationsPossible(e)
        self.assertEqual(ans,res)

    

if __name__ == "__main__":
    unittest.main()