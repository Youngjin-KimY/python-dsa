from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        # Input: temperatures = [73,74,75,71,69,72,76,73]
        # Output: [1,1,4,2,1,1,0,0]

        for i in range(len(temperatures) - 1, -1, -1):
            d = temperatures[i]
        
            while stack and stack[-1][0] <= d:
                stack.pop()
                # diff += 1
            
            # if len(stack) == 0:
            #     diff = 0
            if len(stack) == 0:
                stack.append((d,i))
                res.insert(0, 0)
            else:
                res.insert(0,stack[-1][1] - i)
                stack.append((d, i))
        return res

# lst = [1,2,3,4,5]

# for i in range(len(lst) - 1, -1 , -1):
#     print(lst[i])

# a = (1,2)
# print(a[0])
# print(a[1])