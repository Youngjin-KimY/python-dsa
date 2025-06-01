from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        if grid[0][0] == 0 and len(grid) - 1 == 0:
            return 1
        dx = [-1,-1,-1,0,0,1,1,1]
        dy = [1,0,-1,1,-1,1,0,-1]
        
        start = (0,0, 1)
        endpointXY = len(grid)-1
        q = deque([])
        q.append(start)
        grid[0][0] = 1
        border = len(grid) - 1
        pathDis = 100000000
        while len(q) > 0:
            cx, cy, pathLeng = q.popleft()
            for i in range(0, len(dx)):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or ny < 0 or nx > border or ny > border:
                    continue
                if grid[ny][nx] == 0:
                    if nx == endpointXY and ny == endpointXY:
                        pathDis = min(pathDis,pathLeng + 1)
                    grid[ny][nx] = 1
                    q.append((nx,ny, pathLeng + 1))

        return -1 if pathDis==100000000 else pathDis