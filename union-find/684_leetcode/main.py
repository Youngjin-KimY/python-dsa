from typing import List

from unionfind import unionfindrank as uf

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        s = set([])
        for edge in edges:
            s.add(edge[0])
            s.add(edge[1])
        
        n = len(s) + 1
        uff = uf(n)
        res: List[List[int]] = []
        for edge in edges:
            v = edge[0]
            u = edge[1]
            if uff.connected(v,u) == False:
                 uff.union(v,u)
            else:
                res.append(edge)
        
        return res[-1]