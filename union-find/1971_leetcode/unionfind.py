from typing import List

class unionfind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(0, n)]
        
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x:int, y:int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            
            self.parent[rootY] = rootX
        # print(self.parent)
    
    def connected(self, x:int, y:int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        return True if rootX == rootY else False

    def print_unionfind(self) -> None:
        print(self.parent)