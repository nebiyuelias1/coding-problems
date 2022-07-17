from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_a = list1
        current_b = list2
        
        start = None
        
        if not list1:
            return list2
        elif not list2:
            return list1
        
        while current_a != None and current_b != None:
            if current_a.val > current_b.val:
                if start is None:
                    start = current_b 
                temp = current_b.next
                current_b.next = current_a
                current_b = temp
                
            else:
                if start is None:
                    start = current_a 
                temp = current_a.next
                current_a.next = current_b
                current_a = temp
                
        return start
    

list1_five = ListNode(val=5)

list2_four = ListNode(val=4)
list2_two = ListNode(val=2, next=list2_four)
list2_one = ListNode(val=1, next=list2_two)

s = Solution()
s.mergeTwoLists(list1_five, list2_one)
