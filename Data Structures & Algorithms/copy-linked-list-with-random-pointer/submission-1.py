"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        hash_ = {}

        curr = head
        while curr:
            hash_[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hash_[curr].next = hash_[curr.next] if curr.next else None
            hash_[curr].random = hash_[curr.random] if curr.random != None else None
            curr = curr.next
        return hash_[head]