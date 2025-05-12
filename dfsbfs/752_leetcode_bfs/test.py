import unittest
from main import Solution
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def testStartPoint(self):
        
        res = self.instance.plusMius("0000", 1, 0)
        expect = "1000"
        self.assertEqual(expect, res)

    def testStartPoint1(self):    
        res = self.instance.plusMius("0000", -1, 0)
        expect = "9000"
        self.assertEqual(expect, res)

    def testStartPoint2(self):    
        res = self.instance.plusMius("0900", 1, 1)
        expect = "0000"
        self.assertEqual(expect, res)
    
    def testStartPoint3(self):    
        res = self.instance.plusMius("0080", -1, 2)
        expect = "0070"
        self.assertEqual(expect, res)

    def test1(self):
        grid = ["0201","0101","0102","1212","2002"]
        target = "0202"
        res = self.instance.openLock(grid, target)
        expect: int = 6
        self.assertEqual(res, expect)

    def test2(self):
        grid = ["8888"]
        target = "0009"
        res = self.instance.openLock(grid, target)
        expect: int = 1
        self.assertEqual(res, expect)

    def test3(self):
        grid = ["8887","8889","8878","8898","8788","8988","7888","9888"]
        target = "8888"
        res = self.instance.openLock(grid, target)
        expect: int = -1
        self.assertEqual(res, expect)

if __name__ == "__main__":
    unittest.main()

