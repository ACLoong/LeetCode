# 032.Longest Valid Parentheses

**<font color=red>level: Hard</font>**

## Description

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()" Output: 2 Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

## C++ Solution

* Time complexity O(n)
* Space complexity O(n)

```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int max_len = 0;
        int last = -1;
        stack<int> left;
        
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') { 
                left.push(i);
            } else {
                // have no matching char
                if (left.empty()) {
                    last = i;
                } else {
                // find the matching char, pop the one
                    left.pop();
                    if (left.empty()) {
                        max_len = max(max_len, i-last);
                    } else {
                        max_len = max(max_len, i-left.top());
                    }
                }
            }
        }
        return max_len;
    }
};
```

##Result 
* Success
* Details:

Runtime: 8 ms, faster than 62.71% of C++ online submissions for Longest Valid Parentheses.


