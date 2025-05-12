import unittest
from main import Solution
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from node import TreeNode

from typing import List
from collections import deque

class test(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def buildTree(self, root: List[int]) -> TreeNode | None:
        if len(root) == 0 or root[0] == None or not root:
            return None
        rootNode = TreeNode(root[0])        
        q = deque([rootNode])
        list_ptn = 1
        while len(q) > 0 and list_ptn < len(root):
            current: TreeNode = q.popleft()

            if current != None:
                if root[list_ptn] != None:
                    current.left = TreeNode(root[list_ptn])
                    q.append(current.left)
                list_ptn = list_ptn + 1

                if root[list_ptn] != None:
                    current.right = TreeNode(root[list_ptn])
                    q.append(current.right)
                list_ptn = list_ptn + 1
            else:
                list_ptn += 2

        return rootNode

    def test1(self):
        root = [3,9,20,None,None,15,7]
        rootNode = self.buildTree(root)
        
        res = self.instance.levelOrder(root=rootNode)
        ans = [[3],[9,20],[15,7]]
        self.assertEqual(res, ans)

    def test3(self):
        root = [1,2,3,4,None,None,5]
        rootNode = self.buildTree(root)
        
        res = self.instance.levelOrder(root=rootNode)
        ans = [[1],[2,3],[4,5]]
        self.assertEqual(res, ans)

if __name__ == "__main__": 
    unittest.main()

