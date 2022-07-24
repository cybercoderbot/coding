"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Algorithm
The above algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers. The first pointer advances the list by n+1n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by nn nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the nnth node counting from the last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.

"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head
        for _ in range(n):
            first = first.next
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
