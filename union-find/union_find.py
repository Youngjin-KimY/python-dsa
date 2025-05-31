from typing import TypeVar


class union_find:
    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(0, size)]
    
    def find(self, x: int):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, x:int, y:int) -> None:
        rootX = self.parent[x]
        rootY = self.parent[y]

        if rootX == rootY:
            return
        
        self.parent[rootY] = rootX
    

    def connected(self, x:int, y:int) -> bool:
        res = False
        if self.parent[x] == self.parent[y]:
            res = True
        else:
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX == rootY:
                res = True
            else:
                res =  False
        return res
    
    def print_union(self) -> None:
        print(self.parent)



