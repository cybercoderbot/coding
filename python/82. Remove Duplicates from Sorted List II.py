"""
82. Remove Duplicates from Sorted List II
Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
 
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use frequency Counter for node vals
        The linked list could be sorted or unsorted
        """

        if not head or not head.next:
            return head

        freq = defaultdict(int)
        node = head
        res = []

        while node:
            freq[node.val] += 1
            node = node.next

        for i in freq:
            if freq[i] == 1:
                res.append(i)

        if not res:
            return None

        node = head = ListNode(res[0])
        for i in range(1, len(res)):
            node.next = ListNode(res[i])
            node = node.next

        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Define two pointers slow and fast. If fast points at a duplicate node, remove this node.
        Time complexity O(N)
        Space complexity O(1)

        """
        slow = fast = dummy = ListNode(None, head)
        prev = None
        while fast:
            if fast.val == prev or (fast.next and fast.val == fast.next.val):
                slow.next = fast.next  # remove duplicate node
            else:
                slow = slow.next
            prev = fast.val
            fast = fast.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This implementation is similar to that of 83. Remove Duplicates from Sorted List. 
        One key difference is that a dummy node is used here, since it is possible to remove head.
        """
        dummy = node = ListNode(next=head)
        while node and node.next:
            temp = node.next
            while temp and node.next.val == temp.val:
                temp = temp.next
            if node.next.next == temp:
                node = node.next
            else:
                node.next = temp
        return dummy.next
