"""
501. Find Mode in Binary Search Tree
Easy

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return

        stack = [(root, -inf, inf)]
        freq = Counter()
        while stack:

            node, low, high = stack.pop()

            if not node:
                continue

            freq[value] += 1
            # freq[value] = freq.get(value, 0) + 1

            stack.append((node.left, low, value))
            stack.append((node.right, value, high))

        mode = max(freq.values())
        return [key for key, val in freq.items() if val == mode]
