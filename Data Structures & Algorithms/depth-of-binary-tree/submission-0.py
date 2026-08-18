# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_ = 0
        
        def inorder(root, curr_max, max_):
            if not root:
                max_ = max(max_, curr_max)
                return max_
            
            max_ = max(inorder(root.left, curr_max + 1, max_), inorder(root.right, curr_max + 1, max_))

            return max_
        
        return inorder(root, 0, 0)