from typing import List, Tuple

class Solution:

    def __init__(self):
        self.dx=[-1,0,0,1]
        self.dy=[0,1,-1,0]
        self.stack: List[Tuple[int,int]] = []

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin: int = image[sr][sc]
        self.runDfs(image, sr, sc, color, origin)

        return image
    
    def runDfs(self, image: List[List[int]], sr: int, sc: int, color: int, origin: int):
        if image[sr][sc] == color:
            return
        
        image[sr][sc] = color
        self.stack.append((sr,sc))
        while len(self.stack) > 0:
            (sr, sc) = self.stack.pop()
            i: int = 3
            while i >= 0:
                newSr = sr + self.dy[i]
                newSc = sc + self.dx[i]
                i = i - 1
                
                if newSc >= len(image[0]) or newSc < 0 or newSr >= len(image) or newSr < 0:
                    continue
                if image[newSr][newSc] == origin:
                    image[newSr][newSc] = color
                    self.stack.append((sr,sc))
                    sr = newSr
                    sc = newSc
                    i = 3

if __name__ == "__main__":

    stack: List[Tuple[int,int]] = []
    stack.append((1,2))
    stack.append((2,2))
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)