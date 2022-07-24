"""
145. Binary Tree Postorder Traversal
Easy

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res
