"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree 
is a binary tree in which the left and right subtrees of every node differ in height by 
no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @lru_cache(None)
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        x, y = self.height(root.left), self.height(root.right)
        return left and right and abs(x - y) <= 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Post-order traverse the tree. 
        At each node, collect the info if its left and right subtrees are 
        balanced and their height. Return 
        1. if the current sub-tree is balanced;
        2. the height of the current sub-tree.
        Time: O(N), Space: O(N)
        """
        @lru_cache(None)
        def check(node):
            """Return True if subtree is balanced and its height."""
            if not node:
                return True, 0

            left, x = check(node.left)
            right, y = check(node.right)

            height = max(x, y) + 1
            balanced = left and right and abs(x - y) <= 1

            return balanced, height

        res, _ = check(root)

        return res
