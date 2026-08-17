class ListNode:
        def __init__(self, val = -1, key = -1, next = None, prev = None):
            self.val = val
            self.key = key
            self.next = next
            self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_ = {}
        self.left, self.right = ListNode(), ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.dim = capacity
    
    def remove(self, node):
        l, r = node.prev, node.next
        l.next = r
        r.prev = l
    
    def insert(self, node):
        l, r = self.right.prev, self.right
        l.next = node
        r.prev = node
        node.next = r
        node.prev = l

    def get(self, key: int) -> int:
        curr = self.hash_.get(key, ListNode())

        if curr.val == -1:
            return -1
        
        self.remove(curr)
        self.insert(curr)

        return curr.val

    def put(self, key: int, value: int) -> None:
        if self.hash_.get(key, ListNode()).val != -1:
            self.remove(self.hash_[key])

        curr = ListNode(value, key)
        self.insert(curr)
        self.hash_[key] = curr

        if len(self.hash_) > self.dim:
            lru = self.left.next
            self.remove(lru)
            del self.hash_[lru.key]

        















        