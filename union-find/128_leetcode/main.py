from typing import List

class uff:
    def __init__(self, nums: List[int]) -> None:
        self.parent = {}
        self.rank = {}
        for i in nums:
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, x: int) -> int | None:
        if self.parent.get(x) == None:
            return None
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x:int, y:int) -> None:
        if self.find(x) == self.find(y):
            return
        
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        
    def connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = uff(nums)

        for key in nums:
            key_m = key - 1
            key_p = key + 1
            if uf.find(key_m) != None:
                if uf.connected(key, key_m) == False:
                    uf.union(key, key_m)
                
            if uf.find(key_p) != None:
                if uf.connected(key, key_p) == False:
                    uf.union(key, key_p)
        
        subMax: int = 0
        for k, v in uf.rank.items():
            subMax = max(subMax, v)
        
        return subMax
    

# paaa = {}
# paaa[1] = 'a'
# paaa[2] = 'b'
# paaa[3] = 'c'

# for k,v in paaa.items():
#     print(k,v)
