from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        n = len(nums)
        res = []
        # visited = [False for _ in range(0,n)]
        # used = set([])
        ing = []
        def permute(idx: int):
            if idx == n:
                if ing not in res:
                    res.append(ing[:])
            
            for a in counter.keys():
                if counter[a] == 0:
                    continue
                ing.append(a)
                counter[a] -= 1
                permute(idx + 1)
                counter[a] += 1
                ing.pop()
    
    
        permute(0)


        return res
    

# a = [1,3,2]

# l= [[1,2,3]]
# if a in l:
#     print(True)