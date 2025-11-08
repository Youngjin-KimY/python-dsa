from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        n = len(points)
        if n == 0:
            return 0
        
        points.sort(key=lambda x: x[1])
        # print(points)
        res = 1
        prev_end = points[0][1]
        for i in range(1, n):

            if prev_end < points[i][0]:
                res += 1
                prev_end = points[i][1]
        
        return res

        # if not points:
        #     return 0

        # # 1. 끝나는 지점을 기준으로 정렬
        # points.sort(key=lambda x: x[1])

        # arrows = 1
        # prev_end = points[0][1]

        # for start, end in points[1:]:
        #     # 현재 풍선이 이전 화살 범위 밖이면 새 화살
        #     if start > prev_end:
        #         arrows += 1
        #         prev_end = end

        # return arrows
            

    


# a,b = [1,2]
# print(a,b)
# ss = set([(1,2),(3,4)])
# for entry in ss:
#     a,b = entry
#     ss.remove(entry)
#     print(ss)