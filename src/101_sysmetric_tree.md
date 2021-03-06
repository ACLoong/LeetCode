## Symmetric Tree

### Description

```Python
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
```

### Python Solutions

#### Approach 1: Recursive

* Time complexity : O(n)
* Space complexity : O(n)

```Python
class Solution(object):
    def is_symmetric(self, root):
        """
        Given a binary tree, check whether it is a mirror of itself

        Args:
            root(TreeNode): The root of tree
        
        Returns:
            a bool value: True or False
        """
        if root is None:
            return True
        return self.symmetric(root.left, root.right)
        
    def symmetric(self, root1, root2):
        if root1 is None or root2 is None:
            if root1 is None and root2 is None:
                return True
            else:
                return False
        if root1.val == root2.val:
            return self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)
        else:
            return False
```

#### Approach 2: Iterative

* Time complexity : O(n)
* Space complexity : O(n)

```Python
class Solution(object):
    def is_symmetric(self, root):
       """
        Given a binary tree, check whether it is a mirror of itself
        
        Args:
            root(TreeNode): The root of tree
        
        Returns:
            a bool value: True or False
        """
        lst = []
        lst.append(root)
        lst.append(root)
        while len(lst) != 0:
            t1 = lst.pop()
            t2 = lst.pop()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            lst.append(t1.left)
            lst.append(t2.right)
            lst.append(t1.right)
            lst.append(t2.left)
        return True
```

### C++ solutions

