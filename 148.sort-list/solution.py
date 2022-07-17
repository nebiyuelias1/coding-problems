from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rec(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        slow = start
        fast = start
        
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
            
        if start == end:
            return
            
        self.rec(start, slow)
        self.rec(slow.next, end)
        
        left_start = start
        right_start = slow.next
        
        while True:
            if not left_start or not right_start:
                break
            
            if left_start == slow.next:
                break
                
            if left_start.val > right_start.val:
                temp = left_start.val
                left_start.val = right_start.val
                right_start.val = temp
                left_start = left_start.next
            else:
                right_start = right_start.next
                
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.rec(head, None)
        
        return head
    
three = ListNode(val=3)
one = ListNode(val=1, next=three)
two = ListNode(val=2, next=one)
four = ListNode(val=4, next=two)

s = Solution()
s.sortList(four)
