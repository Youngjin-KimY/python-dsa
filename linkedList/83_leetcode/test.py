import unittest
from typing import List, Optional
from main import Solution
from ListNode import ListNode

class Test(unittest.TestCase):
    def setUp(self):
        self.ins = Solution()

    def linkedlist(self, inputlist: List[int]) -> Optional[ListNode]:
        head: ListNode = ListNode(inputlist[0])
        cur = head

        for i in range(1, len(inputlist)):
            cur.next = ListNode(inputlist[i])
            cur = cur.next    
        
        return head
    
    def NodetoList(self, head:ListNode) -> List[int]:
        res = []
        cur = head
        while cur != None:
            res.append(cur.val)
            cur =cur.next
        
        return res

    def test1(self):
        t1 = [1,1,2]
        inputNodes = self.linkedlist(t1)
        
        res = self.ins.deleteDuplicates(inputNodes)
        resList = self.NodetoList(res)
        ans = [1,2]
        self.assertEqual(resList, ans)

    def test2(self):
        t1 = [1,1,2,3,3]
        inputNodes = self.linkedlist(t1)
        
        res = self.ins.deleteDuplicates(inputNodes)
        resList = self.NodetoList(res)
        ans = [1,2,3]
        self.assertEqual(resList, ans)

    def test3(self):
        t1 = [1,1,1]
        inputNodes = self.linkedlist(t1)
        
        res = self.ins.deleteDuplicates(inputNodes)
        resList = self.NodetoList(res)
        ans = [1]
        self.assertEqual(resList, ans)
    
if __name__ == "__main__":
    unittest.main()