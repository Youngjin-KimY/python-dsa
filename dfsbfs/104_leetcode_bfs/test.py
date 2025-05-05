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

    def buildTree(self, root: List[int]) -> TreeNode:
        if root[0] == None or not root:
            return
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

    def printTree(self, node: TreeNode):
        print(node.val)

        if(node.left is not None):
            self.printTree(node.left)
        if(node.right is not None):
            self.printTree(node.right)


    def test1(self):
        root = [3,9,20,None,None,15,7]
        rootNode = self.buildTree(root)
        self.printTree(rootNode)
        res = self.instance.maxDepth(root=rootNode)
        expect: int = 3
        self.assertEqual(res, expect)
    
    def test2(self):
        root = [3,9,20,None,None,15,7,None,None,None,None,1,2]
        rootNode = self.buildTree(root)
        self.printTree(rootNode)
        res = self.instance.maxDepth(root=rootNode)
        expect: int = 4
        self.assertEqual(res, expect)


if __name__ == "__main__":
    unittest.main()

