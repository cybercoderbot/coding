"""
333. Largest BST Subtree
Medium

Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.

 

Example 1:
Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.

Example 2:
Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2
"""


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        """
        Traverse the tree in post-order. At each node, we figure out if the sub-tree is a valid BST. 
        If so, we compare its size with the largest BST seen so far.

        Time complexity: O(N)
        Space complexity: O(N)
        """

        def traverse(node):
            """
            Return a few parameters of sub-tree rooted at node.
            BST? | size | low | high 
            """
            nonlocal res

            if not node:
                return True, 0, inf, -inf

            valid1, size1, low1, high1 = traverse(node.left)
            valid2, size2, low2, high2 = traverse(node.right)

            valid = valid1 and valid2 and high1 < node.val < low2
            size = size1 + size2 + 1
            res = max(res, size) if valid else res
            low, high = min(low1, node.val), max(node.val, high2)

            return valid, size, low, high

        res = 0
        traverse(root)

        return res
