from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False for _ in range(0,n)]
        res = []
        self.runPermute(nums,visited, res, [], n)
        return res

    def runPermute(self, nums: List[int], visited: List[bool], res: List[List[int]], ing: List[int], ln: int):
        if len(ing) == ln:
            res.append(ing[:])
            return

        for i in range(0, len(nums)):
            if visited[i] == False:
                ing.append(nums[i])
                visited[i] = True
                self.runPermute(nums,visited, res, ing, ln)
                ing.pop()
                visited[i] = False