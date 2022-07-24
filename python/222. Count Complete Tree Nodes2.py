
"""
222. Count Complete Tree Nodes
Medium

5311

322

Add to List

Share
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution: Essentially, at any node,

compute its height h;
compute the height of its right child

2.1) if it is h-1, then we know the left sub-tree is perfectly balanced whose nodes can be computed using its height;
2.2) it it is h-2 then we know the right sub-tree is perfectly balanced;

"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        hroot = self.height(root)
        hright = self.height(root.right)

        if hright == hroot-1:
            return pow(2, hroot-1) + self.countNodes(root.right)
        else:
            return pow(2, hroot-2) + self.countNodes(root.left)

    def height(self, node: TreeNode) -> int:
        """Return height of given node"""
        res = 0
        while node:
            res += 1
            node = node.left
        return res
