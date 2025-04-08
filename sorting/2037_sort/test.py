import unittest

from main import Solution

class test(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.test_instance = Solution()

    def test1(self):
        seats = [2,2,6,6]
        students = [1,3,2,6]
        ans = self.test_instance.minMovesToSeat(seats, students)
        self.assertEqual(ans, 4)

    def test2(self):
        seats = [4,1,5,9]
        students = [1,3,2,6]
        ans = self.test_instance.minMovesToSeat(seats, students)
        self.assertEqual(ans, 7)    

    def test3(self):
        seats = [3,1,5]
        students = [2,7,4]
        ans = self.test_instance.minMovesToSeat(seats, students)
        self.assertEqual(ans, 4)    

if __name__ == "__main__":
    unittest.main()