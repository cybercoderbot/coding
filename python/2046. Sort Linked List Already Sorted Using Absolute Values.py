"""
2046. Sort Linked List Already Sorted Using Absolute Values
Medium

Given the head of a singly linked list that is sorted in non-decreasing order using the absolute values of its nodes, return the list sorted in non-decreasing order using the actual values of its nodes.
 
Example 1:
Input: head = [0,2,-5,5,10,-10]
Output: [-10,-5,0,2,5,10]
Explanation:
The list sorted in non-descending order using the absolute values of the nodes is [0,2,-5,5,10,-10].
The list sorted in non-descending order using the actual values is [-10,-5,0,2,5,10].

Example 2:
Input: head = [0,1,2]
Output: [0,1,2]
Explanation:
The linked list is already sorted in non-decreasing order.

Example 3:
Input: head = [1]
Output: [1]
Explanation:
The linked list is already sorted in non-decreasing order.
"""


class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We use below naive method to collect values into an array, 
        Sort the array and reconstruct a new linked list with sorted values.

        The solution is the same as 
        148. Sort List

        Time: O(NlogN)
        Space:  O(N)  
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
