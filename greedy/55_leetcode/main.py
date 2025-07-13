from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach_limit = nums[0]

        for i in range(n):
            if reach_limit < i:
                return False

            reach_limit = max(i+nums[i], reach_limit)
            if reach_limit >= n-1:
                return True


        return True