# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList_recursive(self, head):
        """
        Reverse a singly linked list.

        Args:
            head(ListNode): the head node of the linklist

        Returns:
            the head node of the reversed linklist(ListNode)
        """
        if head == None or head.next == None:
            return head
        new_head = self.reverseList_recursive(head.next)
        next_node = head.next             # head -> next_node 
        next_node.next = head             # head <- next_node 
        head.next = None                  # [x] <- head <- next_node
        return new_head

    def reverseList_iterative(self, head):
        """
        Reverse a singly linked list.

        Args:
            head(ListNode): the head node of the linklist

        Returns:
            the head node of the reversed linklist(ListNode)
        """
        pre = None
        cur = head

        while cur != None:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat

        return pre  

    def createList(self):
        """
        Create a linklist

        Args:
            None

        Returns：
            the head node of the linklist
        """
        head = ListNode(0)
        cur = head
        for i in range(1, 10):
            cur.next = ListNode(i)
            cur = cur.next
        return head

    def printList(self, head):
        """
        Print the linklist

        Args:
            head(ListNode): the head node of the linklist

        Returns:
            void
        """
        cur = head
        while cur != None:
            print(cur.val, '-->', end='')
            cur = cur.next

        print('NULL')


if __name__ == "__main__":
    head = Solution().createList()
    Solution().printList(head)
    res_1 = Solution().reverseList_recursive(head)
    Solution().printList(res_1)
    print("------------------------分隔符-----------------------------")
    head = Solution().createList()
    Solution().printList(head)
    res_2 = Solution().reverseList_iterative(head)
    Solution().printList(res_2)
