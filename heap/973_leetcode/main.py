from typing import List
import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x:x[0]*x[0] + x[1]*x[1])
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     points.sort(key=lambda x:x[0]*x[0] + x[1]*x[1])

    #     return points[:k]
    # def calculateDisSquare(self, x:int, y:int)->float:
    #     return math.sqrt(pow(x,2) + pow(y,2))

    # def makedict(self, points: List[int]) -> List[tuple[int:int]]:
    #     distance: List[tuple[int,int]] = []
    #     for i in range(0, len(points)):
    #         dis: int = self.calculateDisSquare(points[i][0],points[i][1])
    #         distance.append((dis,i))
        
    #     return distance


    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     distance: List[tuple[int:int]] = []

    #     distance = self.makedict(points=points)

    #     h = []
    #     for d in distance:
    #         heapq.heappush(h, d)

    #     idx = 0
    #     res = []
    #     for _ in range(0, k):
    #         dis,idx = heapq.heappop(h)
    #         res.append(points[idx])        

    #     return res
    


# a = 2
# print(pow(a,3))