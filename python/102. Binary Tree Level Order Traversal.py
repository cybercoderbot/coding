"""
102. Binary Tree Level Order Traversal
Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return

        res, queue = [], [root]

        while queue:
            level, vals = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            queue = level
            res.append(vals)

        return res
