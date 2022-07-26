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


"""
It takes 3 steps to achive O(N) time and O(1) space for this problem.

locate the mid-point;
reverse the 2nd half;
merge 1st and 2nd half.
"""


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
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


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        # 解题思路：
        # 1. 利用快慢指针找到链表中点mid，将链表分为左右两半
        # 2. 将链表的右半部分in place reverse
        # 3. merge链表的左右两部分

        if not head or not head.next:
            return

        # Find mid point
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # cut the list in the middle
        left = head
        right = mid.next
        if not right:
            return head
        mid.next = None

        # reverse the right half
        node = right.next
        right.next = None
        while node:
            next = node.next
            node.next = right
            right = node
            node = next

        # merge left and right
        dummy = ListNode(None)
        while left or right:
            if left:
                dummy.next = left
                left = left.next
                dummy = dummy.next

            if right:
                dummy.next = right
                right = right.next
                dummy = dummy.next
