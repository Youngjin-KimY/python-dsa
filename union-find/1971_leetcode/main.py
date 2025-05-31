from typing import List
from unionfind import unionfind as uf

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        link_uf = uf(n)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            link_uf.union(u,v)

        return link_uf.connected(source, destination)