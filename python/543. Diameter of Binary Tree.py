"""
543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


Example 2:
Input: root = [1,2]
Output: 1
"""


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def traverse(node):
            """Return length+1 and diameter rooted at node"""
            if not node:
                return 0, 0

            depth1, diameter1 = traverse(node.left)
            depth2, diameter2 = traverse(node.right)
            depth = max(depth1, depth2) + 1
            diameter = max(diameter1, diameter2, depth1 + depth2)

            return depth, diameter

        return traverse(root)[1]


class Solution(object):
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def depth(node):
            """
            Compute depth of the tree
            """
            nonlocal res

            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            res = max(res, left+right)

            return max(left, right) + 1

        res = 0
        depth(root)

        return res
