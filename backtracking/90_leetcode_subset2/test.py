import unittest

from main import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.ins = Solution()

    
    def test1(self):
        t1 = [1,2,2]
        r = self.ins.subsetsWithDup(t1)
        ans = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        
        flag = True
        for el in r:
            if el not in ans:
                flag = False
                break

        if len(ans) != len(r):
            flag = False

        self.assertTrue(flag)

    def test2(self):
        t = [0]
        r = self.ins.subsetsWithDup(t)
        ans = [[],[0]]
        self.assertEqual(r,ans)
    

if __name__ == "__main__":
    unittest.main()