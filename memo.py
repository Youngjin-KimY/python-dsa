from typing import List
import random
import heapq
from collections import deque

# ransomNote = "aab"
# magazine = "baa"
# d = {}
# for w in ransomNote:
#     if w in d.keys():
#         d[w] = d[w]+1
#     else:
#         d.setdefault(w,1)

# for w in magazine:
#     if w in d.keys():
#         if d[w] > 0:
#             d[w] = d[w] - 1
#         else:
#             return False
#     else:
#         return False

t = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

t.sort(key=lambda x: (-x[0],x[1]))

print(t)

