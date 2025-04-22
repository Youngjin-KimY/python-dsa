from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_len: int = 0
        mini_len: int = 10000000
        achive_flag: bool = False
        # target: int = 7
        # nums: List[int] = [2,3,1,2,4,3]
        for i in range(0, len(nums)):
            sub_sum: int = 0
            for j in range(i, len(nums)):
                if sub_sum >= target:
                    achive_flag = True
                    break
                sub_len = sub_len + 1
                sub_sum = sub_sum + nums[j]
        
            if sub_sum >= target:
                achive_flag = True
                mini_len = min(mini_len, sub_len)
        
            sub_len = 0
            sub_sum = 0

        if achive_flag == False:
            mini_len = 0

        return mini_len