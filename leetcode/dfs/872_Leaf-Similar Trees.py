# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root,l):
            if not root:
                return
            dfs(root.left,l)
            if not root.left and not root.right:
                l.append(root.val)
            dfs(root.right,l)
        l1 = []
        l2 = []
        dfs(root1,l1)
        dfs(root2,l2)
        return l1 == l2
