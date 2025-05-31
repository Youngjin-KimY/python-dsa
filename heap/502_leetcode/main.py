from typing import List

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # used = [False for _ in range(0, len(capital))]

        idx = 0
        h = []
        for i in range(0, k):
            # h = []
            for j in range(idx, len(capital)):
                if capital[j] <= w:
                    heapq.heappush(h, (-profits[j], capital[j], j))
                    idx += 1
                else:
                    break
            
            if len(h) > 0:
                maxV, c, idx = heapq.heappop(h)
                # used[idx] = True
                w += (-maxV)
            # while len(h) > 0:
            #     heapq.heappop(h)




        return w
    
# h = []

# # heapq.heappush(h,(1,2,3))
# a,b,c = heapq.heappop(h)
# print(a)
# print(b)
# print(c)

a = [5,4,3,1,0,7]
b = [1,2,3,4,5,6]
c = sorted(zip(a,b))
print(c)