from typing import List

class Solution:
    def isSafe(self, x: int, y: int, board: List[List[str]]) -> bool:
        n = len(board)
        
        dx, dy = x-1, y-1
        while dx >= 0 and dy >= 0:
            if board[dy][dx] == 'Q':
                return False
            dx -= 1
            dy -= 1
        
        dx, dy = x+1, y-1
        while dx < n and dy >= 0:
            if board[dy][dx] == 'Q':
                return False
            dx += 1
            dy -= 1
        
        dy = y-1
        while dy >= 0:
            if board[dy][x] == 'Q':
                return False
            dy -= 1

        return True
    
    def merge(self, board: List[List[str]]) -> List[str]:
        res = []
        n: int = len(board)
        
        for i in range(n):
            r = ''
            for j in range(n):
                r += board[i][j]
            res.append(r)

        return res


    def solveNQueens(self, n: int) -> List[List[str]]:
        board: List[List[str]] = [["." for _ in range(n)] for _ in range(n)]

        res: List[List[str]] = []
        def dfs(row: int):
            if row == n:
                onesetboard = self.merge(board)
                res.append(onesetboard)

                return
            
            for col in range(n):
                if self.isSafe(col, row, board):
                    board[row][col] = 'Q'
                    dfs(row+1)
                    board[row][col] = '.'
            
        dfs(0)

        return res


# a = ['a','v','c']
# t = ''
# for i in range(3):
#     t += a[i]
# print(t)
