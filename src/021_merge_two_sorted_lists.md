## Merge Two Sorted Lists

### Description

```Python
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

    Input: 1->2->4, 1->3->4

    Output: 1->1->2->3->4->4
```

### Python Solutions

#### Approach : Recursive

* Time complexity : O(n)
* Space complexity : O(n)

```Python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Merge two sorted linked lists and return it as a new list

        Args:
            l1(ListNode): the head node of the linklist l1
            l2(ListNode): the head node of the linklist l2
        
        Returns:
            A new list that is made by splicing together the nodes of the first two lists
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
```

## C++ Solutions

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
	for (ListNode *p = &head; l1 != nullptr || l2 != nullptr; p = p->next) {
		int val1 = (l1 == nullptr ? INT_MAX : l1->val);
		int val2 = (l2 == nullptr ? INT_MAX : l2->val); 
		if (val1 <= val2) {
                        p->next = l1;
                        l1 = l1->next;
                } else {
                        p->next = l2;
                        l2 = l2->next;
                }
        }	
	return head.next;
    }
};
```

**Submissions**

* Success
* Details:  
Runtime: 8 ms, faster than 88.15% of C++ online submissions for Merge Two Sorted Lists.