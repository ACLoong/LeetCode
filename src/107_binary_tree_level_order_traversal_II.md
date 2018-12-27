# 107. Binary Tree Level Order Traversal II

**<font color=red>level: Easy</font>**

## Description
```c++
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
```

## C++ Solutions

### Approach 1 : Recursion

* Time complexity: O(n)
* Space complexity: O(n)

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        traverse(root, 1, res);
        reverse(res.begin(), res.end());
        return res;
    }
    void traverse(TreeNode *root, size_t level, vector<vector<int>> &res) {
        if (nullptr == root) {
            return;
        }
        if (level > res.size()) {
            res.push_back(vector<int>());
        }
        res[level - 1].push_back(root->val);
        traverse(root->left, level + 1, res);
        traverse(root->right, level + 1, res);
    }
};
```

**Submissions**

* Success
* Details:  
Runtime: 4 ms, faster than 98.74% of C++ online submissions for Binary Tree Level Order Traversal II.

### Approach 2 : Iteration

* Time complexity: O(n)
* Space complexity: O(n)

```c++
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (nullptr == root) {
            return res;
        }
        queue<TreeNode*> cur;
        queue<TreeNode*> next;
        vector<int> level;
        
        cur.push(root);
        while (!cur.empty()) {
            TreeNode *node = cur.front();
            cur.pop();
            level.push_back(node->val);
            if (nullptr != node->left) {
                next.push(node->left);
            }
            if (nullptr != node->right) {
                next.push(node->right);
            }
            //if the cur is null,swap
            if (cur.empty()) {
                res.push_back(level);
                level.clear();
                swap(cur, next);
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

**Submissions**

* Success
* Details:  
Runtime: 4 ms, faster than 98.74% of C++ online submissions for Binary Tree Level Order Traversal II.