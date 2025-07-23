from typing import List

class Solution:
    def returnKey(self,x: List) -> int:
        return x[1]
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=self.returnKey)

        n = len(intervals)
        cntRemovedItem = 0
        i = 1
        prev = intervals[0]
        while i < n:
            if prev[1] > intervals[i][0]:
                cntRemovedItem += 1
                
            else:
                prev = intervals[i]
            i+=1
        
        return cntRemovedItem
    


s = Solution()

# a = [[1,2],[3,4],[5,3]]
# print(a.sort(key=s.key))
# print(a)