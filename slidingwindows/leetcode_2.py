from typing import List, Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub: int = 0
        chc: Set[str] = set([])
        sub_c: int = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in chc:
                    chc.add(s[j])
                    sub_c += 1
                else:
                    max_sub = max(max_sub, sub_c)
                    sub_c = 0
                    chc.clear()
                    break
        max_sub = max(max_sub, sub_c)
        return max_sub

# a: str = "abcdberq"
# for s in range(0, len(a)):
#     print(a[s])

# a: set = set([])
# a.add(1)
# a.add(2)
# a.add(1)

# if 1 in a:
#     print("good")

# a.clear()

# if 1 in a:
#     print("good2")
# else:
#     print("hu")