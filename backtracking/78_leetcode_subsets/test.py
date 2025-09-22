import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        t1 = [1,2,3]
        r = self.ins.subsets(t1)
        ans = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        flag = True
        for el in r:
            if el not in ans:
                flag = False
                break

        self.assertTrue(flag)

    def test2(self):
        t = []
        r = self.ins.subsets(t)
        ans = [[]]
        self.assertEqual(r,ans)
    

if __name__ == "__main__":
    unittest.main()