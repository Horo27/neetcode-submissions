"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        from collections import deque
        found = {}
        found[node] = Node(node.val)
        que = deque()
        que.append(node)

        while que:
            dim = len(que)
            for _ in range(dim):
                curr = deque.popleft(que)
                for nbr in curr.neighbors:
                    if nbr not in found:
                        found[nbr] = Node(nbr.val)
                        que.append(nbr)
                    found[curr].neighbors.append(found[nbr])
        return found[node]

