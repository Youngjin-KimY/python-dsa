import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        n = [2,3,1,1,4]
        res = self.test_instance.canJump(n)
        ans = True
        self.assertEqual(res,ans)

    def test2(self):
        n = [3,2,1,0,4]
        res = self.test_instance.canJump(n)
        ans = False
        self.assertEqual(res,ans)

    def test3(self):
        n = [2,0,0]
        res = self.test_instance.canJump(n)
        ans = True
        self.assertEqual(res,ans)
        


    def test4(self):
        n = [3,0,8,2,0,0,1]
        res = self.test_instance.canJump(n)
        ans = True
        self.assertEqual(res,ans)


if __name__ == "__main__":
    unittest.main()