from typing import List

import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x : (-x[0],x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        
        return res
        # people.sort(key=lambda x : x[1])
        # n = len(people)
        # res = []
        # p = people[0]
        # q = []
        # q.append(p)
        # for i in range(1, n):
        #     c = people[i]
        #     # while p[1] == c[1]:
        #     #     heapq.heappush(q, c)
        #     if p[1] == c[1]:
        #         heapq.heappush(q,c)
        #     else:
        #         while q:
        #             res.append(heapq.heappop(q))
        #         heapq.heappush(q,c)
        #     p = people[i]
        
        # while q:
        #     res.append(heapq.heappop(q))

        # return res
    



# a = [[1,3],[2,1],[4,5]]
# a.sort(key=lambda x: x[1])
# print(a0)