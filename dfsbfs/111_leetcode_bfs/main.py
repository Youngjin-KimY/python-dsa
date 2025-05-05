from typing import Optional
# from node import TreeNode
import os
import sys
from collections import deque
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from node import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = deque([root])
        depth: int = 0
        while len(q) > 0:
            depth += 1

            for _ in range(0, len(q)):
                c : TreeNode = q.popleft()
                if c.left == None and c.right == None:
                    return depth

                if c.left != None:
                    q.append(c.left)
                
                if c.right != None:
                    q.append(c.right)
        
        return depth