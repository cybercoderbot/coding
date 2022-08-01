"""
445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def list2num(node):
            """Return number represented by linked list."""
            res = 0
            while node:
                res = 10*res + node.val
                node = node.next
            return res

        vals = str(list2num(l1) + list2num(l2))
        dummy = node = ListNode()
        for x in vals:
            node.next = ListNode(int(x))
            node = node.next
        return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 2 - reversed linked-lists (2. Add Two Numbers)
        """

        def reverse(node):
            """Reverse a linked list."""
            prev = None
            while node:
                prev, node.next, node = node, prev, node.next
            return prev

        l1, l2 = reverse(l1), reverse(l2)
        carry = 0
        dummy = node = ListNode()
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, x = divmod(carry, 10)
            node.next = node = ListNode(x)
        return reverse(dummy.next)
