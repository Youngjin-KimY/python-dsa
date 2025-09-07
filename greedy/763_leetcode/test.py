import unittest

from main import Solution

class test(unittest.TestCase):
    def setUp(self):
        self.test_instance = Solution()

    def testTrasformation(self):
        s = "ababcbacadefegdehijhklij"
        t = self.test_instance.transformation(s)
        print(t)
    
    def testTrasformation2(self):
        s = "eccbbbbdec"
        t = self.test_instance.transformation(s)
        print(t)

    def test1(self):
        t1 = "ababcbacadefegdehijhklij"
        res=self.test_instance.partitionLabels(t1)
        ans = [9,7,8]
        self.assertEqual(res,ans)

    def test2(self):
        t1 = "eccbbbbdec"
        res=self.test_instance.partitionLabels(t1)
        ans = [10]
        self.assertEqual(res,ans)


if __name__ == "__main__":
    unittest.main()