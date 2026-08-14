# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1, c2 = l1, l2
        carry = 0
        dummy = prev = ListNode(0)
        

        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            value = (v1 + v2 + carry) % 10
            prev.next = ListNode(value)
            prev = prev.next

            carry = (v1 + v2 + carry) // 10
            
            
            if c1:
                c1 = c1.next 
            if c2:
                c2 = c2.next 
        
        return dummy.next