"""
92. Reverse Linked List II
Medium


Share
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
 

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""



class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        
        prev, cur = dummy, head
        for _ in range(left - 1):
            cur = cur.next
            prev = prev.next
        
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
        