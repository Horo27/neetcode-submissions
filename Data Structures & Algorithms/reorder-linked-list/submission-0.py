# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        head1 = head
        head2 = prev

        while head1 and head2:
            tmp1, tmp2 = head1.next, head2.next

            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2

    
        
        
