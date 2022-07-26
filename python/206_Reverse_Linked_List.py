# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Iterative Method:
        # use a loop, traverse the whole list, reverse the link at each step. That is,
        # adjust the link of the node, to make it point to the previous node instead of the next node

        # head: a global variable of type "pointer to node" (accessible to all functions).
        # It stores the address of head node
        # reverse a linked list: not moving the data, but reversing the links

        # Test corner cases
        if not head:
            return None
        if not head.next:
            return head

        prev = None
        current = head

        while current:
            # cur_next: local pointer variable
            cur_next = current.next
            current.next = prev
            # reset previous and current pointers
            prev = current
            current = cur_next
        head = prev
        return head
