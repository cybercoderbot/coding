"""
109. Convert Sorted List to Binary Search Tree
Medium
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        108. Sorted Array to Binary Search Tree.
        """
        def convert(i, j):
            """Return BST using nums[i:j]"""
            if i == j:
                return None
            mid = (i + j) // 2
            left = convert(i, mid)
            right = convert(mid+1, j)
            return TreeNode(val=nums[mid], left=left, right=right)

        return convert(i=0, j=len(nums))


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        109. Sorted List to Binary Search Tree.
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def convert(i, j):
            """Return node constructed from nums[i:j]"""
            if i == j:
                return None
            mid = (i + j) // 2
            left = convert(i, mid)
            right = convert(mid+1, j)
            return TreeNode(val=nums[mid], left=left, right=right)

        return convert(i=0, j=len(nums))
