"""
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Define two pointers prev initialized to be None, and node initialized at head. 
        Reverse the pointing of node to prev and keep track of node.next in the meantime. 
        Move both prev and node.
        """
        prev = None
        node = head
        while node:
            node.next, node, prev = prev, node.next, node
        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We use below naive method to collect values into an array, 
        Reverse the array and reconstruct a new linked list with reversed values.

        The solution is the similar to
        148. Sort List

        Time: O(NlogN)
        Space:  O(N)  
        """

        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        dummy = node = ListNode()
        for x in nums[::-1]:
            node.next = ListNode(x)
            node = node.next

        return dummy.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        cur = head
        while cur:
            oldnext = cur.next
            cur.next = pre
            pre = cur
            cur = oldnext

        return pre
