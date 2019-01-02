# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        Given a singly linked list, determine if it is a palindrome.

        Args:
            head(ListNode): the head node of the linklist

        Returns:
            A bool value
        """
        if head == None or head.next == None:
            return True

        lat = head.next
        pre = head
        while lat != None and lat.next != None:
            lat = lat.next.next
            pre = pre.next

        cur = pre.next
        pre.next = None
        p = None
        while cur != None:
            q = cur.next
            cur.next = p
            p = cur
            cur = q

        while p != None and head != None:
            if p.val != head.val:
                return False
            p = p.next
            head = head.next

        return True