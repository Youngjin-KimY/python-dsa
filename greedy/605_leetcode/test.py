import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def test1(self):
        f = [1,0,0,0,1]
        n = 1
        res = self.test_instance.canPlaceFlowers(f,n)
        ans = True
        self.assertEqual(res,ans)

    def test2(self):
        f = [1,0,0,0,1]
        n = 2
        res = self.test_instance.canPlaceFlowers(f,n)
        ans = False
        self.assertEqual(res,ans)

    def test3(self):
        f = [1,1,1,1,1]
        n = 1
        res = self.test_instance.canPlaceFlowers(f,n)
        ans = False
        self.assertEqual(res,ans)

    def test4(self):
        f = [1,1,1,1,1]
        n = 0
        res = self.test_instance.canPlaceFlowers(f,n)
        ans = True
        self.assertEqual(res,ans)

    def test5(self):
        f = [1,0,0,0,1,0,0]
        n = 2
        res = self.test_instance.canPlaceFlowers(f,n)
        ans = True
        self.assertEqual(res,ans)


if __name__ == "__main__":
    unittest.main()