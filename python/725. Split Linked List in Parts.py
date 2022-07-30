"""
725. Split Linked List in Parts
Medium

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        N = 0
        node = head
        while node:
            node = node.next
            N += 1

        # r implies how many extra nodes cannot be fit.
        # N=8, k=3  ==> [3, 3, 2]
        # 8 % 3 = 2 ==> it has 2 mroe nodes can't be fit
        #               r = 2 slots starting from the front will have one more.
        chunk, extra = divmod(N, k)

        res = []
        for i in range(k):

            if extra >= 1:
                size = chunk + 1
            else:
                size = chunk
            extra -= 1

            res.append(head)
            last = None
            while size > 0:
                last = head
                head = head.next
                size -= 1
            if last:
                last.next = None

        return res
