# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = str(root.val)
        que = deque()        
        que.append(root)
        while que:
            dim = len(que)
            for _ in range(dim):
                curr = que.popleft()
                res += ","
                res += str(curr.left.val) if curr.left else "*"
                res += ","
                res += str(curr.right.val) if curr.right else "*"
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
        for i in range(len(res) - 1, -1, -1):
            if res[i] not in "*,":
                return res[:i+1]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return
        arr = data.split(',')
        que = deque()
        head = TreeNode(arr[0])
        que.append(head)
        
        i = 1
        while i < len(arr):
            curr = que.popleft()
            if arr[i] != "*":
                curr.left = TreeNode(arr[i])
                if curr.left:
                    que.append(curr.left)
            i += 1
            if i < len(arr) and arr[i] != "*":
                curr.right = TreeNode(arr[i])
                if curr.right:
                    que.append(curr.right)
            i += 1
        return head




