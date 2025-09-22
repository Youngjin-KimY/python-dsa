import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    def test1(self):
        n = 3
        r = self.ins.generateParenthesis(n)
        ans = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(r,ans)

    def test2(self):
        n = 1
        r = self.ins.generateParenthesis(n)
        ans = ["()"]
        self.assertEqual(r,ans)

    def test3(self):
        n = 2
        r = self.ins.generateParenthesis(n)
        ans = ["(())","()()"]
        self.assertEqual(r,ans)

    # def testSubFunc1(self):
    #     charst = "((()))"
    #     res = self.ins.isValidParenthsis(charst)
    #     self.assertTrue(res)
    
    # def testSubFunc2(self):
    #     charst = "())(()"
    #     res = self.ins.isValidParenthsis(charst)
    #     self.assertFalse(res)

    # def testSubFunc3(self):
    #     charst = "((((()"
    #     res = self.ins.isValidParenthsis(charst)
    #     self.assertFalse(res)
    # def testSubFunc4(self):
    #     charst = "(())))"
    #     res = self.ins.isValidParenthsis(charst)
    #     self.assertFalse(res)
    # def testSubFunc5(self):
    #     charst = "()))))"
    #     res = self.ins.isValidParenthsis(charst)
    #     self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()