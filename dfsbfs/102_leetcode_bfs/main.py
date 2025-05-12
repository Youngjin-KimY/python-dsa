from typing import Optional, List
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        res = [[root.val]]
        while len(q) > 0:
            sub = []
            for _ in range(0, len(q)):
                current: TreeNode = q.popleft()
                if current.left is not None:
                    q.append(current.left)
                    sub.append(current.left.val)
                if current.right is not None:
                    q.append(current.right)
                    sub.append(current.right.val)
            if len(sub) > 0:
                res.append(sub)

        return res
# lst = [1,2,'null']
# for i in range(0, len(lst)):
#     print(lst[i])

# lst = [1,2,3]
# for i in range(0, len(lst)):
#     print(lst[i])
#     lst.append(100)

