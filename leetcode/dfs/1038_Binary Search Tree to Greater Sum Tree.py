class Solution(object):
    def convertBST(self, root):
        self.sum = 0
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left)
        dfs(root)
        return root
