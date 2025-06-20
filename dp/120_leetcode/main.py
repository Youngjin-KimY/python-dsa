from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = [0] * (n+1) # avoiding index out of range for bottom line 

        for i in range(n-1,-1,-1):
            for j in range(len(triangle[i])):
                m[j] = triangle[i][j] + min(m[j],m[j+1])

        return m[0]
    
