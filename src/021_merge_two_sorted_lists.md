# 021.Merge Two Sorted Lists

**<font color=red>level: Easy</font>**

## Description

Merge two sorted linked lists and return it as a new list. e new list should be made by splicing together the nodes of the first two lists.

## Solution in C++

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head(-1);
	for( ListNode* p= &head; l1!= nullptr || l2 != nullptr; p=p->next){
		int val1 = l1 == nullptr ? INT_MAX : l1->val;
		int val2 = l2 == nullptr ? INT_MAX : l2->val; 
		if(val1 <= val2){
			p->next = l1;
			l1 = l1->next;
		}else{
			p->next = l2;
			l2 = l2->next;
		}
	}	
	return head.next;
    }
};

```
## Result
* Success
* Details:

Runtime: 8 ms, faster than 88.15% of C++ online submissions for Merge Two Sorted Lists.


