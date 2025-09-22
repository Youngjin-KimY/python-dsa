from typing import List, Tuple

class Solution:

    def deepcopy2d(self, chessBoard: List[List[str]]) -> List[List[str]]:
        n = len(chessBoard)
        tmp = [["." for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                tmp[y][x] = chessBoard[y][x]
        
        return tmp

    def checkRoomAndNumQeen(self, chessBoard: List[List[str]]) -> Tuple[bool, int]:
        x = len(chessBoard[0])
        y = len(chessBoard)
        resRoom = False
        resNumQueen = 0
        for yy in range(y):
            for xx in range(x):
                if chessBoard[yy][xx] == 'Q':
                    resNumQueen+=1
                if chessBoard[yy][xx] == '.':
                    resRoom = True
        
        return (resRoom, resNumQueen)
    

    def convertChessBoard(self, chessBoard: List[List[str]]) -> List[List[str]]:
        res = []
        n = len(chessBoard)
        
        tmp = self.deepcopy2d(chessBoard)

        for y in range(n):
            for x in range(n):
                if chessBoard[y][x] == 'X':
                    tmp[y][x] = '.'
            res.append(''.join(tmp[y]))
        
        return res
    
    def blockChessBoard(self, x: int, y: int, chessBoard: List[List[str]]) -> List[List[str]]:
        n = len(chessBoard)
        
        for dx in range(len(chessBoard)):
            if chessBoard[y][dx] == '.':
                chessBoard[y][dx] = 'X'
        
        for dy in range(len(chessBoard)):
            if chessBoard[dy][x] == '.':
                chessBoard[dy][x] = 'X'
        
        dx, dy = x-1, y-1
        while True:
            if dx < 0 or dy < 0:
                break
            chessBoard[dy][dx] = 'X'
            dx -= 1
            dy -= 1
        
        dx, dy = x+1, y+1
        while True:
            if dx >= n or dy >= n:
                break
            chessBoard[dy][dx] = 'X'
            dx += 1
            dy += 1
        
        dx, dy = x+1, y-1
        while True:
            if dx >= n or dy < 0:
                break
            chessBoard[dy][dx] = 'X'
            dx += 1
            dy -= 1


        dx, dy = x-1, y+1
        while True:
            if dx < 0 or dy >= n:
                break
            chessBoard[dy][dx] = 'X'
            dx -= 1
            dy += 1
        
        return chessBoard

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        inner = []
        chessBoard = []

        for __ in range(n):
            for _ in range(n):
                inner.append('.')
            chessBoard.append(inner[:])
            inner = []


        def backracking(beforeChessBoard: List[List[str]]):
            isRoom, numQ = self.checkRoomAndNumQeen(beforeChessBoard)
            if not isRoom:
                if n == numQ:
                    convertedChessboard = self.convertChessBoard(beforeChessBoard)
                    
                    if convertedChessboard not in res:
                        res.append(convertedChessboard)

                    return
            newChessBoard = self.deepcopy2d(beforeChessBoard)
            for y in range(n):
                for x in range(n):
                    if beforeChessBoard[y][x] == '.':
                        newChessBoard[y][x] = 'Q'
                        filledblockChessBoard = self.blockChessBoard(x,y,newChessBoard)
                        backracking(self.deepcopy2d(filledblockChessBoard))
                        newChessBoard = self.deepcopy2d(beforeChessBoard)

        backracking(chessBoard)

        return res

# a = "...."
# a = list(a)
# b = a[:]
# b[0] = 'a'
# print(''.join(a), ''.join(b))
        