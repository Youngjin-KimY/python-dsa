from typing import List
from collections import Counter


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ing: List[int] = []
        res: List[List[int]] = []
        n = len(candidates)
        def dfs(idx: int):
            if sum(ing) == target:
                res.append(ing[:])
                return
            
            for i in range(idx, n):
                ing.append(candidates[i])
                dfs(i+1)
                ing.pop()
                
        
        dfs(0)

        return res 