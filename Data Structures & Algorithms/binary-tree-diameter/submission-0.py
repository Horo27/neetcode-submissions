# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = 0

        def dfs(node):
            nonlocal height

            if not node:
                return 0
            
            maxl = dfs(node.left)
            maxr = dfs(node.right)
            height = max(maxr + maxl, height)

            return 1 + max(maxl, maxr)
        
        dfs(root)
        return height