from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []
        n = len(nums)
        def backtracking(idx: int):
            if idx == len(nums):
                return
            
            for i in range(idx, n):
                sub.append(nums[i])
                res.append(sub[:])

                backtracking(i + 1)
                
                sub.pop()
        res.append(sub[:])
        backtracking(0)

        return res

        
        