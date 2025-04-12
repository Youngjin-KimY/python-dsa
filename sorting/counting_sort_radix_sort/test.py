import unittest
from typing import List

from counting_sort import counting_sort

class test(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.sol = counting_sort()
    
    def test(self):
        t1: List[int] = [2,5,3,0,2,3,0,3]
        ans = self.sol.counting_sort(t1)
        self.assertEqual([0,0,2,2,3,3,3,5], ans)
    
    def test2(self):
        t2: List[int] = [10,2,1,2,4,5,6,11,2,12,22,100]
        ans = self.sol.counting_sort(t2)
        self.assertEqual([1,2,2,2,4,5,6,10,11,12,22,100], ans)
if __name__ == "__main__":
    unittest.main()