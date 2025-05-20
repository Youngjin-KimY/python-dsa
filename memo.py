from typing import List
import random

lst: List[int] = [1,5,3,2,4,6,7,9]

pivotIdx = random.randint(0, 7)

pivot= lst[pivotIdx]
print("pivot", pivot)
lst[pivotIdx], lst[len(lst) - 1] = lst[len(lst) - 1], lst[pivotIdx]

startIdx = 0
for i in range(0, len(lst)):
    if pivot > lst[i]:
        lst[startIdx], lst[i] = lst[i], lst[startIdx]
        startIdx += 1


lst[len(lst) - 1], lst[startIdx] = lst[startIdx], lst[len(lst) - 1]
print(startIdx)
print(lst)