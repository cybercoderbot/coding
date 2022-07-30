"""
530. Minimum Absolute Difference in BST
Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""


class Solution:
    def getMinimumDifference(self, root):
        """Inorder Recursion"""

        def dfs(node):
            if node.left:
                dfs(node.left)
            nums.append(node.val)
            if node.right:
                dfs(node.right)

        nums = []
        dfs(root)

        return min(b - a for a, b in zip(nums, nums[1:]))


class Solution(object):
    def getMinimumDifference(self, root):
        """
        Keep track of the low and high bounds of each node, when you've passed the leaf nodes, 
        compute high - low to get the lowest difference along that path
        """

        def dfs(node, low, high):
            if not node:
                return high - low

            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return min(left, right)

        return dfs(root, -inf, inf)
