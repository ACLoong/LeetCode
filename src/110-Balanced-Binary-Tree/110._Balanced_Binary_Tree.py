# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if abs(self.TreeDepth(root.left) - self.TreeDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
       
    def TreeDepth(self, root):
        if root == None:
            return 0
        Left = self.TreeDepth(root.left)
        Right = self.TreeDepth(root.right)
        return max(Left, Right) + 1
