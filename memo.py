from typing import List
import random
import heapq
from collections import deque

h = [6,3,2,1,5,7]
q = deque(h)
a = heapq.heapify(h)

print(q)
print(h)
q.popleft()
print(q)
print(h)