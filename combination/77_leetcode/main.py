from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def commb(i: int, path: List[int]):
            if len(path) == k:
                res.append(path[:])
                return
            
            for x in range(i, n+1):
                path.append(x)
                commb(x+1, path)
                path.pop()

        commb(1, [])

        return res