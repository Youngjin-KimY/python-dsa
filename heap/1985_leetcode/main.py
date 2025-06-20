from typing import List

import heapq


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        inums = []
        
        for i in range(0, len(nums)):
            heapq.heappush(inums, -int(nums[i]))

        for _ in range(0, k-1):
            heapq.heappop(inums) 

        return str(-heapq.heappop(inums))   