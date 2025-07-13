import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        g = []
        c = []
        res=self.test_instance.canCompleteCircuit(g,c)
        ans = 0
        self.assertEqual(res,ans)
        

    def test2(self):
        pass

    def test3(self):
        pass

if __name__ == "__main__":
    unittest.main()