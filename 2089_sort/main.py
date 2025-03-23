from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for x in range(0, len(nums)):
            if nums[x] == target:
                res.append(x)

        return res