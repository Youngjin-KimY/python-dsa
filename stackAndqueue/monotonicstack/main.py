from typing import List

class MonotonicStack:

    def __init__(self):
        self.ms = []
    
    def monotonicIncreasing(self, nums: List[int]) -> List[int]:
        res: List[int] = []
        s: List[int] = []

        for num in nums:

            while s and s[-1] > num:
                s.pop()
            s.append(num)
        
        while s:
            res.insert(0, s.pop())

        return res

ms = MonotonicStack()
nums = [3, 1, 4, 1, 5, 9, 2, 6]
res = ms.monotonicIncreasing(nums=nums)
print(res)