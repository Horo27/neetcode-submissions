# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        next_ = prev

        while next_:
            for i in range(k):
                next_ = next_.next
                if not next_:
                    return dummy.next
            nnext = next_.next
            nprev = prev.next
            next_.next = None

            i = prev.next
            j = i.next

            while j:
                aux = j.next
                j.next = i
                i = j
                j = aux
            
            prev.next = i
            nprev.next = nnext
            prev = nprev
            next_ = prev
        return dummy.next


            
            

