from typing import List

class uf:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(0,n+1)]
    
    def find(self, x: int) -> int:
        parentX = self.parent[x]
        
        if parentX != x:
            self.parent[x] = self.find(parentX) #  parentX is not root
        
        return self.parent[x]
    
    def union(self, x:int, y:int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX

    def connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)




class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n: int = len(isConnected)
        uff = uf(n)
        for i in range(0,len(isConnected)):
            for j in range(0, len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    if uff.connected(i,j) == False:
                        uff.union(i,j)
        
        s = set([])
        for i in range(0, n):
            root = uff.find(i)
            s.add(root)

        return len(s)