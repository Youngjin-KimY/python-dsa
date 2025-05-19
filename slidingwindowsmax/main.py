from typing import List

import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:



        res: List[int] = []
        h: List[int] = []
        eIdx = 0

        if len(nums) <= k:
            for i in range(0, len(nums)):
                heapq.heappush(h, -nums[i])
            
            return [-heapq.heappop(h)]


        for i in range(0, len(nums) - k + 1):
            # [1,3,-1,-3,5,3,6,7]
            while eIdx - i < k and eIdx < len(nums):
                heapq.heappush(h, -nums[eIdx])
                eIdx += 1
            subMax = -heapq.heappop(h)
            res.append(subMax)
            heapq.heappush(h, -subMax)
            
            h.remove(-nums[i])
            heapq.heapify(h)



        return res
    
hq = []

heapq.heappush(hq, 3)
heapq.heappush(hq, 5)
heapq.heappush(hq, 1)
heapq.heappush(hq, 19)

print(hq)
print(hq.pop())
print(hq.remove(1))
print(hq)