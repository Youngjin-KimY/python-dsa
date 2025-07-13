from typing import List

import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(0, k):
            s = heapq.heappop(nums)
            heapq.heappush(nums, -s)
        
        res = 0
        for i in range(0, len(nums)):
            res += nums[i]

        return res
    
        # important thing is that case of thing which is smallest value 
        # with minus flag is also smallest


        # nums.sort()
        # dq = deque(nums)
        # for i in range(0, k):
        #     if dq[0] == 0:
        #         continue
        #     else:
        #         tmp = dq.popleft()
        #         dq.append(-tmp)
            
        # return sum(dq) 