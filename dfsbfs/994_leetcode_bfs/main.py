from typing import List, Tuple
# from node import TreeNode
import os
import sys
from collections import deque
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x == other.x) and (self.y == other.y)
         
    def __hash__(self):
        return hash((self.x, self.y))

class Solution:

    def findRottenPointList(self, grid: List[List[int]]) -> List[Point]:
        res: List[Point] = []

        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == 2:
                    res.append(Point(x,y))

        return res

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dx = [-1,0,0,1]
        dy = [0,-1,1,0]

        time: int = 0

        startPointList: List[Point] = self.findRottenPointList(grid)

        if len(startPointList) == 0:
            ## [[0]] =0 , [[1,0]] =-1
            for y in range(0, len(grid)):
                for x in range(0, len(grid[0])):
                    if grid[y][x] == 1:
                        return -1
            return 0            


        q = deque([])
        for i in range(0, len(startPointList)):
            q.append(Point(startPointList[i].x,startPointList[i].y))
        
        while len(q) > 0:
            next: bool = False
            for _ in range(0, len(q)):    
                currentPoint = q.popleft()
                for i in range(0, len(dx)):
                    nX = currentPoint.x + dx[i]
                    nY = currentPoint.y + dy[i]
                    if nX < 0 or nX >= len(grid[0]) or nY < 0 or nY >= len(grid):
                        continue
                    if grid[nY][nX] == 1:
                        q.append(Point(nX, nY))
                        grid[nY][nX] = 2
                        next = True
            if next:
                time += 1

        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == 1:
                    return -1


        return time



# lst = [1,2,'null']
# for i in range(0, len(lst)):
#     print(lst[i])

# lst = [1,2,3]
# for i in range(0, len(lst)):
#     print(lst[i])
#     lst.append(100)

a = Point(1,1)
b = Point(1,1)
if a == b:
    print("same")