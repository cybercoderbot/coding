"""
965. Univalued Binary Tree
Easy

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:
Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: root = [2,2,2,5,2]
Output: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        res, queue = [], [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return len(set(res)) == 1


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        values = set()
        stack = [root]
        while stack:
            node = stack.pop()
            values.add(node.val)
            if len(values) > 1:
                return False
             if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True 
