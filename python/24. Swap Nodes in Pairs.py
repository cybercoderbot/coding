"""
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:


"""
Here, pre is the previous node. Since the head doesn't have a previous node, I just use self instead. 
Again, a is the current node and b is the next node.

To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. 
Instead of thinking about in what order I change them, I just change all three at once.

"""


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(None)
        dummy.next = head
        pre, pre.next = dummy, head

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return dummy.next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)

        return head
