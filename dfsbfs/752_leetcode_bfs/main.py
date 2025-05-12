from typing import List, Tuple, Set
# from node import TreeNode
import os
import sys
from collections import deque
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return (self.x == other.x) and (self.y == other.y)
         
#     def __hash__(self):
#         return hash((self.x, self.y))

class Solution:
    def plusMius(self, c: str, deltaDigits: int, digitsIndex: int) -> int:
        cDigit = int(c[digitsIndex])
        nDigit = cDigit + deltaDigits
        if nDigit < 0:
            nDigit = 9
        if nDigit == 10:
            nDigit = 0
        return c[:digitsIndex] + str(nDigit) + c[digitsIndex+1:]
                              

    def openLock(self, deadends: List[str], target: str) -> int:
        # deadendsInt = [int(deadends[i]) for i in  range(0, len(deadends))]
        if "0000" in deadends:
            return -1


        deltaDigits = [1, -1, 1, -1, 1, -1, 1, -1]
        visited: Set[int] = set([])

        q = deque(["0000"])
        visited.add("0000")
        time: int = 0

        while len(q) > 0:
            goNext: bool = False
            for i in range(0, len(q)):
                currentData = q.popleft()
                for i in range(0, len(deltaDigits)):
                    # "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
                    newData = self.plusMius(currentData, deltaDigits[i], int(i/2))
                    if newData not in deadends and newData not in visited:
                        q.append(newData)
                        visited.add(newData)
                        goNext = True
                        if newData == target:
                            time += 1
                            return time

            if goNext:
                time += 1


        return -1
    
# a = ["1234","1992","9919", "2199"]
# aa = [int(a[i]) for i in range(0, len(a))]
# print(a)
# print(aa)
# a = "1234"
# aa = "5678"
# b = int(a)
# bb = int(aa)
# print(b)
# print(bb)
# print(b+bb)

# a = "1111"
# print(a)
# print(a[0])
# # a[1] = 2
# # print(a)
# a = a.replace("1", "2", 0)
# print(a)

a = set([1])
b = 1 
if b in a:
    print('a')