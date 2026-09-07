# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ = root.val
        def dfs(node):
            nonlocal max_
            if not node:
                return 0
            
            sum_left = max(0, dfs(node.left))
            sum_right = max(0, dfs(node.right))
            
            max_extendable = node.val + max(sum_left, sum_right)
            max_including = node.val + sum_left + sum_right

            max_ = max(max_, max_including)
            return max_extendable

        dfs(root)
        return max_
                        
