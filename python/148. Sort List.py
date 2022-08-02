"""
148. Sort List
Medium

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        We use below naive method to collect values into an array, 
        Sort the array and reconstruct a new linked list with sorted values.
        The solution is the same as 
        2046. Sort Linked List Already Sorted Using Absolute Values
        Time: O(NlogN), Space:  O(N)  
        """
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        nums.sort()

        dummy = node = ListNode()
        for x in nums:
            node.next = ListNode(x)
            node = node.next

        return dummy.next
