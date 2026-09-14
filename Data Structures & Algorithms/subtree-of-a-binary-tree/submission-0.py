# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return "$"
            return str(node.val) + "#" + dfs(node.right) + dfs(node.left)
        parent = dfs(root)
        child = dfs(subRoot)
        print(parent, child)
        return child in parent
            
        