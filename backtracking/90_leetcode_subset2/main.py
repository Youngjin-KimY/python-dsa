from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sub = []
        res = []
        n = len(nums)
        visited = [False for _ in range(n)]
        def backtracking(idx: int):
            if idx == n:
                return
            
            for i in range(idx, n):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                sub.append(nums[i])
                visited[i] = True
                res.append(sub[:])
                backtracking(i + 1)
                sub.pop()
                visited[i] = False
            
        res.append([])
        backtracking(0)

        return res