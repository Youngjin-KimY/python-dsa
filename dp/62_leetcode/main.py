# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         grid = [[0 for _ in range(0,n+1)] for _ in range(0,m+1)]
#         grid[1][1] = 1

#         for i in range(1,m+1):
#             for j in range(1, n+1):
#                 if i ==1 and j ==1:
#                     continue
#                 grid[i][j] = grid[i-1][j] + grid[i][j-1]

#         return grid[m][n]
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [0 for i in range(0, n+1)]
        memo[1] = 1
        for i in range(0, m):
            for j in range(1, n+1):
                memo[j] = memo[j] + memo[j-1]
                    


        return memo[-1]