from typing import List, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        subArea: int = 0
        maxSubArea: int = 0
        stack:List[Tuple[int,int]] = []

        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == 1:
                    subArea = self.runDFS(x,y,grid,stack,0)
                    maxSubArea = max(subArea, maxSubArea)
                
        return maxSubArea
    
    def runDFS(self, x: int, y:int, grid: List[List[int]], stack: List[Tuple[int,int]], subSum: int):
        dx = [-1,0,0,1]
        dy = [0,1,-1,0]

        if grid[y][x] == 2:
            return
        
        stack.append((x,y))

        while len(stack) > 0:
            x, y = stack.pop()
            # if grid[y][x] == 2:
            #     continue
            subSum = subSum + 1
            grid[y][x] = 2
            for i in range(0, len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= len(grid[0]) or ny >= len(grid) or nx < 0 or ny < 0:
                    continue
                if grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    stack.append((nx, ny))
        
        return subSum
        


