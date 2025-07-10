from typing  import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if flowerbed.count(0) == 0:
            return False

        lenFlowerbed = len(flowerbed)

        cur = 0
        while n > 0 and cur < lenFlowerbed:
            if flowerbed[cur] == 1:
                cur += 2
            else:
                if cur == lenFlowerbed -1 and flowerbed[cur] == 0:
                    n -= 1
                    flowerbed[cur] = 1
                    cur += 2
                elif cur+1 < lenFlowerbed and flowerbed[cur+1] == 0:
                    flowerbed[cur] = 1
                    n -= 1
                    cur += 2
                else:
                    # f[cur] = 0, f[cur+1], so cur move 3
                    cur += 3

        if n == 0:
            return True
        return False
    

# s  =Solution()
# a = s.canPlaceFlowers([],1)
# print(a)