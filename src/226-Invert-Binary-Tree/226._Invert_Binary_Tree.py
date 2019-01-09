# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root):
        """
        Invert a binary tree.

        Args:
            root(TreeNode): the root node of the given tree

        Rerurns:
            the root node of the Invert tree(TreeNode)
        """
        if root is None:
            return None

        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
