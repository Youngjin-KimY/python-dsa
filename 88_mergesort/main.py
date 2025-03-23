from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        sum = []
        while p1 < m and p2 < n:
            if nums1[p1] > nums2[p2]:
                sum.append(nums2[p2])
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                sum.append(nums1[p1])
                p1 += 1
            else:
                sum.append(nums1[p1])
                sum.append(nums2[p2])
                p1 += 1
                p2 += 1
        
        while p1 < m:
            sum.append(nums1[p1])
            p1 += 1
        
        while p2 < n:
            sum.append(nums2[p2])
            p2 += 1
        
        for x in range(0, len(nums1)):
            nums1[x]=sum[x]
        

        print("ans", nums1)


# p1 = 0
# p2 = 0

# # n1 = [1,3,7,8]
# # n2 = [2,4,6,12]
# n1 = [1,2,3,4]
# n2 = [6,7,8,9]
# sum = []
# while p1 < len(n1) and p2 < len(n2):
#     if n1[p1] > n2[p2]:
#         sum.append(n2[p2])
#         p2 += 1
#     elif n1[p1] < n2[p2]:
#         sum.append(n1[p1])
#         p1 += 1
    
# if p1 < len(n1):
#     while p1 < len(n1):
#         sum.append(n1[p1])
#         p1 += 1

# if p2 < len(n2):
#     while p2 < len(n2):
#         sum.append(n2[p2])
#         p2 += 1

# print(sum)

# lst = [1,2,3,4,5]
# lst.insert(1, 10)
# print(lst)