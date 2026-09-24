from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None :
            return root
        queue = deque()
        queue.append(root)
        while queue :
            q = queue.popleft()
            tmp = q.left
            q.left = q.right
            q.right = tmp

            if q.right is not None :
                queue.append(q.right)
            if q.left is not None :
                queue.append(q.left)
        return root