from typing import List



class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = 0
        for x in nums:
            offset += x
        
        dpTable = [0 for _ in range(2*offset + 1)]

        dpTable[offset] = 1 # origin real value 0

        nextTable = [0 for _ in range(2*offset +1)]
        nDpTable = len(dpTable)
        for i in range(1,n+1):
            num = nums[i-1]
            nextTable = [0 for _ in range(nDpTable)]
            for j in range(0, nDpTable):
                if j + num < nDpTable:
                    nextTable[j] += dpTable[j+num]

                if j - num >= 0:
                    nextTable[j] += dpTable[j-num]
                    
            dpTable = nextTable[:]
        
        if target > offset:
            return 0

        return nextTable[offset+target]




#         offset  = 0
#         for x in nums:
#             offset += x
        


#         dpTable = [[0 for _ in range(2 * offset + 1)] 
#                    for _ in range(len(nums) + 1)]


#         dpTable[0][offset] = 1 # origin, using 0 to make 0 -> 1, the others  -> 0
#         border = len(dpTable[0])
#         for i in range(1, len(nums) + 1):
#             n = nums[i-1]
#             for j in range(0, 2 * offset + 1):
#                 if j-n >= 0 and dpTable[i-1][j-n] > 0:
#                     dpTable[i][j] += dpTable[i-1][j-n]
#                 if j+n < border and dpTable[i-1][j+n] > 0:
#                     dpTable[i][j] += dpTable[i-1][j+n]
#                 # if i - 1 >=0 and (j-1) >=0: 
#                 #     dpTable[i][j] += dpTable[i-1][j-1]
#                 # if i - 1 >=0 and (j+1) < len(dpTable[0]):
#                 #     dpTable[i][j] += dpTable[i-1][j+1]
        
#         n = len(nums)

#         if target > offset:
#             return 0

#         return dpTable[n][offset + target]