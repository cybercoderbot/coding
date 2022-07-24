"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

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
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        rootBalanced = abs(self.height(root.left) -
                           self.height(root.right)) <= 1

        return rootBalanced and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Post-order traverse the tree. At each node, collect the info if its left and right sub-trees are 
        balanced and their height. Return 
        1. if the current sub-tree is balanced;
        2. the height of the current sub-tree.

        Time complexity O(N)
        Space complexity O(N)
        """

        def check(node):
            """Return True if subtree is balanced and its height."""
            if not node:
                return True, 0

            balanced1, height1 = check(node.left)
            balanced2, height2 = check(node.right)

            height = max(height1, height2) + 1
            balanced = balanced1 and balanced2 and abs(height1 - height2) <= 1

            return balanced, height

        res, _ = check(root)

        return res
