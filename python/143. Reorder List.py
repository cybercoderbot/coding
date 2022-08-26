"""
143. Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Modify head in-place instead.
        """
        # 1. locate the mid-point
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse the 2nd half
        prev = None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next

        # 3. merge 1st and 2nd half
        node = head
        while prev and prev.next:
            node.next, node = prev, node.next
            prev.next, prev = node, prev.next

        return
