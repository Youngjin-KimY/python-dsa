from typing import List, Optional
from ListNode import ListNode
# Definition for singly-linked list.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        cur: ListNode= head

        while cur != None:
            if cur.next != None and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:    
                cur = cur.next
            
            
        return head
                

        