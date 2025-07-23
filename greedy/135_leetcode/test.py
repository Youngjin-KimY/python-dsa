import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        g = [1,2,3,4,5]
        c = [3,4,5,1,2]
        res=self.test_instance.canCompleteCircuit(g,c)
        ans = 0
        self.assertEqual(res,ans)
        

    def test2(self):
        g = [2,3,4]
        c = [3,4,3]
        res=self.test_instance.canCompleteCircuit(g,c)
        ans = 0
        self.assertEqual(res,ans)

    def test3(self):
        pass

if __name__ == "__main__":
    unittest.main()