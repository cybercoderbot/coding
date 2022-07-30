"""
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        A naive solution is to convert linked list to array and check array. 
        This takes O(N) extra space.
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        A in-place O(1) solution is 
        1) locate middle node
        2) reverse the first half of the list 
        3) compare the nodes by moving pointers forward and backward.
        """

        # 1) locate middle node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2) reverse 2nd half
        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow

        # 3) check for palindrome
        while prev and head.val == prev.val:
            head = head.next
            prev = prev.next

        return not prev
