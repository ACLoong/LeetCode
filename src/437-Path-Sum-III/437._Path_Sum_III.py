# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findPath(self, root, sum):
        """
        Find a path that sum to a given value

        Args:
            root(TreeNode): the root node of the given tree
            sum(int): a integer value that are given

        Returns:
            the number of paths that sum to a given value(int)
        """
        result = 0
        if root is None:
            return result

        if root.val == sum:
            result += 1

        result += self.findPath(root.left, sum - root.val)
        result += self.findPath(root.right, sum - root.val)
        return result

    def pathSum(self, root, sum):
        """
        You are given a binary tree in which each node contains an integer value.

        Find the number of paths that sum to a given value.

        The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

        Args:
            root(TreeNode): the root node of the given tree
            sum(int): a integer value that are given

        Returns:
            the number of paths that sum to a given value(int)
        """
        result = 0
        if root is None:
            return result

        result += self.findPath(root, sum)
        result += self.pathSum(root.left, sum)
        result += self.pathSum(root.right, sum)

        return result
