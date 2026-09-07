# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = 0
        res = None
        def snr(node):
            nonlocal pos
            nonlocal res
            if res:
                return
            if node.left:
                snr(node.left)
            pos += 1
            if pos == k:
                res = node.val
            if node.right:
                snr(node.right)
        snr(root)
        return res