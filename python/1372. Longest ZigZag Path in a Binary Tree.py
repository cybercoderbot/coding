"""
1372. Longest ZigZag Path in a Binary Tree
Medium

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
"""


"""
Algorithm:
Traverse the tree and compute the length of zigzag path ending at a node. 
Return the largest of such value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        """
        Traverse the tree and compute the length of zigzag path ending at a node. 
        Return the largest of such value.
        Store (node, length, isLeft) in stack when traversing the tree
        """
        res = 0
        stack = [(root, 0, None)]
        while stack:
            node, path, left = stack.pop()
            if not node:
                continue
            res = max(res, path)
            if left:
                stack.append((node.left,  1, True))
                stack.append((node.right, path+1, False))
            else:
                stack.append((node.left,  path+1, True))
                stack.append((node.right, 1, False))

        return res
