# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            while head.val == val:
                head = head.next
                if head is None:
                    return head
            q = head
            p = q.next
            while p:
                if p.val == val:
                    q.next = p.next
                else:
                    q = q.next
                p = p.next
        return head
