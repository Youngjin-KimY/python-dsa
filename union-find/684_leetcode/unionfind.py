from typing import List

class unionfindrank:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(0,n)]
        self.rank = [1 for _ in range(0,n)]

    def find(self, x: int) -> int:
        rootX = self.parent[x]

        if rootX != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x: int, y:int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] >= self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1

    def connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
    
    def print_union(self):
        print(self.parent)
        print(self.rank)