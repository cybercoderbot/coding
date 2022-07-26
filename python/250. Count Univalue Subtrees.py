"""
250. Count Univalue Subtrees
Medium

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [5,5,5,5,5,null,5]
Output: 6

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        def isUnival(node, parent):
            """
            Return if a subtree is unival
            """
            nonlocal res

            if not node:
                return True

            left = isUnival(node.left, node.val)
            right = isUnival(node.right, node.val)

            if left and right:
                res += 1

            return left and right and node.val == parent

        res = 0
        isUnival(node=root, parent=None)

        return res
