"""
144. Binary Tree Preorder Traversal
Easy

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 
"""


class Solution(object):
    @lru_cache(None)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        root -> left -> right
        """
        if not root:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        @lru_cache(None)
        def preorder(node):
            if not node:
                return []

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(root)
        return res


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                # right -> left
                stack.append(node.right)
                stack.append(node.left)
        return res


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
