from typing import List
# from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # counter = Counter(candidates)

        n = len(candidates)
        res = []
        ing = []
        visited = [False for _ in range(n)]
        candidates.sort()

        def dfs(idx: int):
            if sum(ing) == target:
                res.append(ing[:])
            
            for i in range(idx,n):
                thisCandid = candidates[i]
                if i > 0 and (thisCandid == candidates[i-1] and visited[i-1] is False):
                    continue
                currSum = sum(ing)

                if thisCandid > target or (thisCandid + currSum) > target:
                    continue
                ing.append(thisCandid)
                visited[i] = True
                dfs(i+1)
                ing.pop()
                visited[i] = False
        dfs(0)

        return res