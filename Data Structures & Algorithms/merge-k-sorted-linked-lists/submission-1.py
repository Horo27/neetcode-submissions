# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not len(lists):
            return None

        dummy = ListNode()
        prev = dummy
        import heapq
        heap = []
        heapq.heapify(heap)

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, NodeWrapper(lists[i]))

        while heap:
            curr = heapq.heappop(heap)

            if curr.node.next:
                heapq.heappush(heap, NodeWrapper(curr.node.next))
            
            prev.next = curr.node
            prev = prev.next
            prev.next = None
        return dummy.next
