import unittest
from main import Solution
from typing import List

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()


    def test1(self):
        tokens = ["2","1","+","3","*"]
        ans = 9
        res = self.instance.evalRPN(tokens=tokens)

        self.assertEqual(res, ans)
    
    def test2(self):
        tokens = ["4","13","5","/","+"]
        ans = 6
        res = self.instance.evalRPN(tokens=tokens)

        self.assertEqual(res, ans)

    def test3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        ans = 22
        res = self.instance.evalRPN(tokens=tokens)

        self.assertEqual(res, ans)

if __name__ == "__main__":
    unittest.main()