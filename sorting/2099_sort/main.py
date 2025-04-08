from typing import List, Tuple
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        picked = {}
        blank = []
        minheap_origin = [-1 * nums[x] for x in range(0, len(nums))]
        for x in range(0, len(nums)):
            key = nums[x]
            if picked.get(key) != None:
                v: List = picked.get(key)
                v.append((x, False))
            else:
                # key = value, x = index, False = visited or not
                picked[key] = [(x, False)]
            blank.append("_")
        
        heapq.heapify(minheap_origin)
        for x in range(0, k):
            max = heapq.heappop(minheap_origin) * -1
            max_list_tuple : List[Tuple[int, int]] = picked.get(max)
            idx = 0
            for x in range(0, len(max_list_tuple)):
                if max_list_tuple[x][1] == False:
                    idx = max_list_tuple[x][0]
                    max_list_tuple[x] = (max_list_tuple[x][0], True)
                    break
            blank[idx] = max
    
        res = [ blank[x] for x in range(0, len(blank)) if blank[x] != "_"]

        return res