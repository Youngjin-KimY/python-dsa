from typing import List

class Solution:

    def __init__(self):
        self.dx=[-1,0,0,1]
        self.dy=[0,1,-1,0]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin: int = image[sr][sc]
        self.runDfs(image, sr, sc, color, origin)
        
        # print(image)
        return image

    def runDfs(self, image: List[List[int]] ,sr: int, sc: int, target: int, origin: int):
        if image[sr][sc] == target:
            return
        image[sr][sc] = target

        for i in range(0, len(self.dx)):
            newSr = sr + self.dy[i]
            newSc = sc + self.dx[i]
            if newSr >= len(image) or newSc >= len(image[0]) or newSr < 0 or newSc < 0:
                continue
        
            if image[newSr][newSc] != target and image[newSr][newSc] == origin:
                self.runDfs(image, newSr, newSc, target, origin)
    