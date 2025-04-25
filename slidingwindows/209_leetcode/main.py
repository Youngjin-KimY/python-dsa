from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sub_sum: int = 0
        mini_len: int = 1000000000
        sub_len: int = 0
        over_target: bool = False

        s_idx: int = 0

        for i in range(0, len(nums)):
            sub_sum = sub_sum + nums[i]
            sub_len = sub_len + 1
            if sub_sum >= target:
                while sub_sum >= target:
                    over_target = True
                    mini_len = min(mini_len, sub_len)
                    sub_sum = sub_sum - nums[s_idx]
                    s_idx = s_idx + 1
                    sub_len = sub_len -1
        
        if not over_target:
            mini_len = 0

        return mini_len
                    


