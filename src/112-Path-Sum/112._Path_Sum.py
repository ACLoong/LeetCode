# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        left_found = False
        right_found = False
        
        if root.left:
            left_found = self.hasPathSum(root.left, sum - root.val)
            
        if root.right:
            right_found = self.hasPathSum(root.right, sum - root.val)
            
        if root.left is None and root.right is None and root.val == sum:
            return True
        
        return left_found or right_found