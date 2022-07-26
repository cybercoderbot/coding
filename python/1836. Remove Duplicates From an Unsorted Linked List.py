"""
1836. Remove Duplicates From an Unsorted Linked List
Medium

Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.

Example 1:
Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].

Example 2:
Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.

Example 3:
Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].
"""


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = defaultdict(int)
        node = head
        while node:
            freq[node.val] += 1
            node = node.next

        dummy = node = ListNode(next=head)
        while node.next:
            if freq[node.next.val] > 1:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next


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
