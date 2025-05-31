from typing import List, Tuple

class uuf:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: str) -> str:
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x: str, y: str) -> None:
        self.parent[self.find(x)] = self.find(y)


    def connected(self, x: str, y: str) -> bool:
        rX = self.find(x)
        rY = self.find(y)
        res = (rX == rY)
        return res

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = uuf()
        q: List[str] = []

        for equ in equations:
            u, v, op = self.parserEquation(equ)

            if op == "==":
                uf.union(u,v)
            else:
                q.append(equ)
                # if uf.connected(u,v) == True:
                #     return False

        for equ in q:
            u, v, op = self.parserEquation(equ)
            if uf.connected(u, v) == True:
                return False

        return True

    def parserEquation(self, eq: str) -> Tuple[str,str,str]:
        return (eq[0], eq[-1], eq[1:-1])
