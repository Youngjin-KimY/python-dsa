import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        t = [2,3,1,1,4]
        res=self.test_instance.jump(t)
        ans = 2
        self.assertEqual(res,ans)

    def test2(self):
        t = [2,3,0,1,4]
        res=self.test_instance.jump(t)
        ans = 2
        self.assertEqual(res,ans)
        

    def test3(self):
        pass

if __name__ == "__main__":
    unittest.main()