"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Given nums, retrieve the number in the middle which is the value for the root.
        Left and right sub-array become left and right sub-tree respectively.
        """
        def convert(i, j):
            """Return BST using nums[i:high]"""
            if i == j:
                return None

            mid = (i + j) // 2
            left = convert(i, mid)
            right = convert(mid+1, j)

            return TreeNode(val=nums[mid], left=left, right=right)

        return convert(0, len(nums))


class Solution:
    def arrayToBST(self, nums: List[int]) -> TreeNode:
        """Sort array -> BST"""
        nums.sort()

        def convert(i, j):
            """Return BST using nums[i:j]"""
            if i == j:
                return None

            mid = (i + j) // 2
            left = convert(i, mid)
            right = convert(mid+1, j)

            return TreeNode(val=nums[mid], left=left, right=right)

        return convert(i=0, j=len(nums))
