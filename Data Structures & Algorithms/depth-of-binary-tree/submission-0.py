# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def walk(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth

        depth += 1

        l = self.walk(node.left, depth)
        r = self.walk(node.right, depth)
        
        return max(l, r)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.walk(root, 0)