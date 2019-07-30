# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        self.depth = float('Inf')
        def dfs(node, level):
            if not node:return
            if not node.right and not node.left:self.depth = min(self.depth, level)
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level+1)
        dfs(root, 1)
        return self.depth