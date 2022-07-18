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
        
        
    
    

list1_five = ListNode(val=5)

list2_four = ListNode(val=4)
list2_two = ListNode(val=2, next=list2_four)
list2_one = ListNode(val=1, next=list2_two)

s = Solution()
s.mergeTwoLists(list1_five, list2_one)
