import unittest

from main import Solution
from typing import List

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.ins = Solution()

    def test1(self) -> None:
        n = 4
        k = 2
        res: List[List[int]] = self.ins.combine(n,k)
        ans = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

        self.assertEqual(res, ans)

if __name__ == "__main__":
    unittest.main()