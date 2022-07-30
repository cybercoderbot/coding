"""
86. Partition List
Medium

Given the head of a linked list and a value target, partition it such that all nodes less than x come before nodes greater than or equal to target.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, target: int) -> ListNode:
        """
        Scan the linked list and store node vals in an array
        """

        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        small = [x for x in nums if x < target]
        large = [x for x in nums if x >= target]
        nums = small + large

        dummy = node = ListNode()
        for x in nums:
            node.next = ListNode(x)
            node = node.next
        return dummy.next


class Solution:
    def partition(self, head: ListNode, target: int) -> ListNode:
        """
        Create two sub-lists, and add them to two list according to node val
        """
        dummy1 = node1 = ListNode()
        dummy2 = node2 = ListNode()
        node = head

        while node:
            if node.val < target:
                node1.next = node
                node1 = node1.next
            else:
                node2.next = node
                node2 = node2.next
            node = node.next

        node1.next = dummy2.next
        node2.next = None

        return dummy1.next


class Solution:
    def partition(self, head: ListNode, target: int) -> ListNode:
        dummy = slow = fast = ListNode(next=head)
        while fast and fast.next:
            if fast.next.val < target:
                if fast == slow:
                    fast = fast.next
                else:
                    # insert fast.next after slow
                    fast.next.next, fast.next, slow.next = slow.next, fast.next.next, fast.next
                slow = slow.next
            else:
                fast = fast.next
        return dummy.next


"""
2161. Partition Array According to Given Pivot

Example 1:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]

Example 2:
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]

"""


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small, equal, large = [], [], []

        for x in nums:
            if x < pivot:
                small.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                large.append(x)

        return small + equal + large
