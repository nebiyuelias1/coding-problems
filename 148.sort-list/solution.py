from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            start = list1
            prev = list1
            main = list1.next
            secondary = list2
        else:
            start = list2
            prev = list2
            secondary = list1
            main = list2.next
        
        while True:
            if secondary == None:
                break
            if main == None:
                prev.next = secondary
                break
            
            if main.val >= secondary.val:
                new_secondary = secondary.next
                prev.next = secondary
                secondary.next = main
                prev = secondary
                secondary = new_secondary
            else:
                main = main.next
                prev = prev.next
                
            
                
        return start
    
    def rec(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        if start == end:
            return start
        
        slow = start
        fast = start
        
        while fast != end and fast and fast.next != end:
            slow = slow.next
            fast = fast.next.next
            
        new_next = slow.next
        slow.next = None
        if end:
            end.next = None
        left_start = self.rec(start, slow)
        right_start = self.rec(new_next, end)
        
        ans = self.mergeTwoLists(left_start, right_start)
        return ans
        
                
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = self.rec(head, None)
        return ans
    
three = ListNode(val=3)
one = ListNode(val=1, next=three)
two = ListNode(val=2, next=one)
four = ListNode(val=4, next=two)

s = Solution()
s.sortList(four)
