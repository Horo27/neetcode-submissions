# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque

        if not root:
            return 0

        que = deque([root])
        max_ = 0

        while que:
            max_ += 1
            lvl = len(que)

            for i in range(lvl):
                curr = que.popleft()
                
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
        return max_