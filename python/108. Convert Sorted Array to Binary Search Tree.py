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


"""
Given nums, retrieve the number in the middle which is the value for the root. 
Left and right sub-array become left and right sub-tree respectively.

"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def build(low, high):
            """Return BST using nums[low:high]"""
            if low == high:
                return None

            mid = (low + high) // 2
            left = build(low, mid)
            right = build(mid+1, high)

            return TreeNode(nums[mid], left, right)

        return build(0, len(nums))
