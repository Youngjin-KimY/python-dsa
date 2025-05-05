from typing import Optional
# from node import TreeNode
import os
import sys
from collections import deque
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = deque([root])
        depth: int = 0

        while len(q) > 0:
            depth = depth + 1
            
            for _ in range(0, len(q)):
                current = q.popleft()
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q.append(current.right)

        return depth

# lst = [1,2,'null']
# for i in range(0, len(lst)):
#     print(lst[i])

# lst = [1,2,3]
# for i in range(0, len(lst)):
#     print(lst[i])
#     lst.append(100)

