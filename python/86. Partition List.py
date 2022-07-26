"""
86. Partition List
Medium

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.


Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""


"""
The algo is simple and clear. Just scan the linked list. The tricky part is how to organize the code concisely to reflect the logic. Below implementation is my best effort.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Use an array
        """
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        vals = [v for v in vals if v < x] + [v for v in vals if v >= x]
        dummy = node = ListNode()
        for x in vals:
            node.next = ListNode(x)
            node = node.next
        return dummy.next

        # dummy = node = ListNode(vals[0])
        # for x in vals[1:]:
        #     node.next = ListNode(x)
        #     node = node.next
        # return dummy


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = slow = fast = ListNode(next=head)
        while fast and fast.next:
            if fast.next.val < x:
                if fast == slow:
                    fast = fast.next
                else:  # insert fast.next after slow
                    fast.next.next, fast.next, slow.next = slow.next, fast.next.next, fast.next
                slow = slow.next
            else:
                fast = fast.next
        return dummy.next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Create two sub-lists like below
        """
        dummy1 = node1 = ListNode()
        dummy2 = node2 = ListNode()
        node = head

        while node:
            if node.val < x:
                node1.next = node1 = node
            else:
                node2.next = node2 = node
            node = node.next
        node1.next = dummy2.next
        node2.next = None
        return dummy1.next


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
