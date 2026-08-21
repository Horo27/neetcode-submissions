# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        que = deque([root])
        result = []

        while que:
            lvl_len = len(que)
            lvl = []
            for _ in range(lvl_len):
                curr = que.popleft()
                lvl.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            result.append(lvl)
        return result