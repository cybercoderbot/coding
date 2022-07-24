"""
270. Closest Binary Search Tree Value
Easy

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.


Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        1. if root.val == target, return root.val;
        2. if root.val > target, move to left subtree. All nodes in right subtree have larger difference than current node
        3. if root.val < target, move to right subtree.

        Time complexity O(N)
        Space complexity O(1)

        """

        res, node = inf, root

        while node:
            if node.val == target:
                return node.val
            res = min(res, node.val, key=lambda x: abs(x-target))

            if node.val < target:
                node = node.right
            else:
                node = node.left

        return res
