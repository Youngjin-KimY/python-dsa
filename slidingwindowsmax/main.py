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

        d = dict()
        for i in range(0, len(nums) - k + 1):
            # [1,3,-1,-3,5,3,6,7]
            while eIdx - i < k and eIdx < len(nums):
                heapq.heappush(h, (-nums[eIdx], eIdx))
                d[eIdx] = nums[eIdx]
                if len(d) > k:
                    d.pop(i-1) 
                eIdx += 1
            
            subMax = 0
            idx = 0
            while True:
                subMax, idx = heapq.heappop(h)
                if idx in d.keys():
                    break
            subMax = -subMax
            res.append(subMax)
            heapq.heappush(h, (-subMax, idx))

            # h.remove(-nums[i])
            # heapq.heapify(h)


        return res
    
# hq = []

# heapq.heappush(hq, 3)
# heapq.heappush(hq, 5)
# heapq.heappush(hq, 1)
# heapq.heappush(hq, 19)

# print(hq)
# print(hq.pop())
# print(hq.remove(1))
# print(hq)hf


# d = dict({1:"a",2:"B",3:"C",4:"D",5:"E"})
# print(len(d))
# d.pop(1)
# print(len(d))
# print(d)