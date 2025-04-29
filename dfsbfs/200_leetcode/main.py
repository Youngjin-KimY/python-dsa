from typing import List

class Solution:

    def __init__(self):
        self.dx = [-1,0,0,1]
        self.dy = [0,1,-1,0]


    def numIslands(self, grid: List[List[str]]) -> int:
        
        xlen = len(grid[0])
        ylen = len(grid)
        numberOfIslands: int = 0

        visited: List[List[bool]] = [ [False for _ in range(0, xlen)] for _ in range(0, ylen)]

        for x in range(0, len(visited[0])):
            for y in range(0, len(visited)):
                if not visited[y][x] and grid[y][x] == "1":
                    numberOfIslands = numberOfIslands + 1
                    self.runDfs(x, y, visited, grid)

        return numberOfIslands

    def runDfs(self, sX: int, sY: int, visited: List[List[bool]], grid: List[List[str]]):
        if visited[sY][sX]:
            return
        
        visited[sY][sX] = True

        for i in range(0, len(self.dx)):
            nSy = sY + self.dy[i]
            nSx = sX + self.dx[i]
            if nSy < len(visited) and nSx < len(visited[0]) and nSy >= 0 and nSx >= 0:
                if visited[nSy][nSx] == False and grid[nSy][nSx] == "1":
                    self.runDfs(nSx, nSy, visited, grid)



        
        






# xlen = 3
# ylen = 4
# visited: List[List[str]] = [ [False for _ in range(0, xlen)] for _ in range(0, ylen)]
        
# print(visited)
    