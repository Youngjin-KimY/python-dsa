from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        curEnd = 0
        curMax = 0
        cntJmp = 0
        n = len(nums)
        for i in range(0, n-1):
            curMax = max(curMax, i + nums[i])

            if i == curEnd:
                cntJmp += 1
                curEnd = curMax

                

        return cntJmp