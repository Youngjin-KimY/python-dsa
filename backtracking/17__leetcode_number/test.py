import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        d = "23"
        r = self.ins.letterCombinations(d)
        ans =  ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(r,ans)

    def test2(self):
        d = ""
        r = self.ins.letterCombinations(d)
        ans =  []
        self.assertEqual(r,ans)

    def test3(self):
        d = "2"
        r = self.ins.letterCombinations(d)
        ans =  ["a","b","c"]
        self.assertEqual(r,ans)
        
if __name__ == "__main__":
    unittest.main()