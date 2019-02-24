# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head)
        if head == None or head.next == None:
            return head

        cur = head
        while cur != None and cur.next != None:
            if(cur.next.val == cur.val):
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return head
