"""
61. Rotate List
Medium

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        N = 0
        node = head
        while node:
            N += 1
            node = node.next

        k %= N
        if not k:
            return head

        fast = slow = head
        while fast.next:
            fast = fast.next
            if k < 1:
                slow = slow.next
            k -= 1

        fast.next, slow.next, head = head, None, slow.next

        return head
