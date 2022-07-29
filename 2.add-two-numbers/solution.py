from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = l1
        two = l2
        
        head = l1
        tail = None
        
        carry = 0
        
        while True:          
            digit_sum = carry
            carry = 0
            
            if one:
                digit_sum += one.val
                
            if two:
                digit_sum += two.val
            
            if digit_sum >= 10:
                carry = 1
                digit_sum -= 10
                
            if one and two:
                one.val = digit_sum
                two.val = digit_sum
                tail = one
                
                one = one.next
                two = two.next
                
            elif one and not two:
                one.val = digit_sum
                tail = one
                
                one = one.next
                
            elif not one and two:
                two.val = digit_sum
                tail = two
                head = l2
                
                two = two.next
                
            if not one and not two:
                break
        
        if carry > 0:
            tail.next = ListNode(val=carry)
            
        return head
            