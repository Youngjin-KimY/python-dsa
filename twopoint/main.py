from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1

            while left < right:
                subSum = nums[i]+nums[left]+nums[right]
                if subSum < 0:
                    left += 1
                elif subSum > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res
# t = [-1,0,1,2,-1,-4] -> -4 -1 -1 0 1 2 

        
        

# from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         m = {}
#         n = len(nums)
#         for i in range(n):
#             if m.get(nums[i]) == None:
#                 m[nums[i]] = 1
#             else:
#                 m[nums[i]] += 1
#             # m[nums[i]] = 1 if m[nums[i]] == None else (m[nums[i]] + 1)
        
#         res = []
#         visited = [False for _ in range(n)]
#         for i in range(n-1):
#             if visited[i]:
#                 continue
#             for j in range(i+1, n-2):
#                 if visited[j]:
#                     continue
#                 remain = 0 - (nums[i] + nums[j])
#                 # cntRemain = m.get(remain)
#                 # if cntRemain != None and cntRemain > 0:
#                 for k in range(j+1, n):
#                     if visited[k]:
#                         continue
#                     else:
#                         if nums[k] == remain:
#                             res.append([nums[i],nums[j],nums[k]])
#                             visited[i], visited[j], visited[j] = True, True, True
        


#         return res
        
        