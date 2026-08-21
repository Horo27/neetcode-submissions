# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque

        que = deque([root])
        result = []

        while que:
            lvl_len = len(que)
            for i in range(lvl_len):
                curr = que.popleft()
                if i == lvl_len - 1:
                    result.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
        return result