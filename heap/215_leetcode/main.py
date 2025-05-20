from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maxValue = max(nums)
        # cntList = [0 for _ in range(0, maxValue + 1)]
        d: dict[int, int] = {}
        for i in range(0, len(nums)):
            if d.get(nums[i]) == None:
                v = nums[i]
                d[v] = 1
            else:
                v = nums[i]
                d[v] += 1
        
        h = []
        # for i in range(1, len(d)):
        #     heapq.heappush(h,(-cntList[i],i))
        for key in d.keys():
            heapq.heappush(h, (-d[key], key))
        
        res = []

        for i in range(0, k):
            pv = heapq.heappop(h)
            res.append(pv[1])

        return res

# h = []
# heapq.heappush(h, (3,43))
# heapq.heappush(h, (2,23))
# heapq.heappush(h, (1,11))
# print(h)
# v = heapq.heappop(h)
# print(v)
# print(v[0])
# print(v[1])

# d = {1:2, 10:1, 21:22}
# print(d.get(1))

# d[1] += 1
# print(d.get(1))

# for key in d.keys():
#     print(key)