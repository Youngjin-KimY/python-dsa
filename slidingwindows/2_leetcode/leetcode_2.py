from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_idx: int = 0
        bucket: Set[str] = set([])
        max_sub_len: int = 0
        sub_len: int = 0
        for i in range(0, len(s)):
            if s[i] not in bucket:
                bucket.add(s[i])
                sub_len = sub_len + 1
                max_sub_len = max(max_sub_len, sub_len)
            else:
                while True:
                    if s[s_idx] == s[i]:
                        s_idx = s_idx + 1
                        break
                    bucket.remove(s[s_idx])
                    s_idx = s_idx + 1
                    sub_len = sub_len - 1
        
        return max_sub_len

# a: dict[int] = {}
# a["a"] = 1
# print(a.get('a'))
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