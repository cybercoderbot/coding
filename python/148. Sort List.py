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


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 常见排序方法:
        # insert sort，selection sort，heap sort，quick sort，bubble sort，merge sort，bucket sort等
        # 它们的时间复杂度不尽相同，而这里题目限定了时间必须为O(nlgn)，
        # 符合要求只有quick sort，merge sort, heap sort，而根据linked list的特点，最适于merge sort

        # 解题思路：
        # merge sort，链表的中点可以通过“快慢指针”法求得

        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        rhead = mid.next
        mid.next = None
        return self.merge(self.sortList(head), self.sortList(rhead))

    def merge(self, lhead, rhead):
        # dummy node
        dummy = ListNode(0)
        head = dummy
        while lhead and rhead:
            if lhead.val < rhead.val:
                head.next = lhead
                lhead = lhead.next
            else:
                head.next = rhead
                rhead = rhead.next
            head = head.next
        if lhead:
            head.next = lhead
        elif rhead:
            head.next = rhead

        return dummy.next

    def get_mid(self, head):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
