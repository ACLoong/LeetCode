# 020.Valid Parentheses

**<font color=red>level: Easy</font>**

## Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

## C++ Solution

* Time complexity O(n)
* Space complexity O(n)

```c++
class Solution {
public:
    bool isValid(string s) {
        string left = "([{";
        string right = ")]}";       
        stack<char> stk;
        
        for (auto c:s) {
            if (left.find(c) != string::npos) {
                stk.push(c);
            } else {
                if (stk.empty() || stk.top() != left[right.find(c)])
                    return false;
                else
                    stk.pop();
            }
        }
        return stk.empty();
    }
};

```

##Result 
* Success
* Details:

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Valid Parentheses.


