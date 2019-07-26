# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        mid = int((len(nums)+1)/2)g
        
        if mid != 0:
            left  = nums[:mid-1]
            right = nums[mid:]
            root = TreeNode(nums[mid-1])
            
            if len(left) != 0 or len(right) != 0:
                root.left  = self.sortedArrayToBST(left)
                root.right = self.sortedArrayToBST(right)
                
            return root