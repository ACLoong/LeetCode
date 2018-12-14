# 002.Add Two Numbers

**<font color=red>level:Medium</font>**

## Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:  
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  
Output: 7 -> 0 -> 8  
Explanation: 342 + 465 = 807.

## C++ Solution 

* Time complexity O(m+n)
* Space complexity O(1)

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(-1);
        ListNode *prev = head;
        int carry = 0;
        int sum = 0;
        while (nullptr != l1 || nullptr != l2) {
            int v1 = (l1 == nullptr ? 0 : l1->val);
            int v2 = (l2 == nullptr ? 0 : l2->val); 
            sum = v1 + v2 + carry;
            carry = sum / 10;
            prev->next = new ListNode(sum % 10);
            prev = prev->next;
            if (nullptr != l1) {
		l1 = l1->next;
	    }
            if (nullptr != l2) { 
		l2 = l2->next;
	    }    
        }
        if (carry==1) {
            prev->next = new ListNode(1);
	}
        return head->next;
    }
};
```

###Submissions  
* Success  
* Details:  
Runtime: 28 ms, faster than 98.57% of C++ online submissions for Add Two Numbers.


