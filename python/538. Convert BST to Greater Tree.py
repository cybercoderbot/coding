"""
538. Convert BST to Greater Tree
Medium

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
"""


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        @lru_cache(None)
        def inorder(node, x):
            """Inorder traverse and update node's value."""
            if not node:
                return x
            x = inorder(node.right, x)  # sum of right subtree
            x += node.val
            node.val = x
            return inorder(node.left, x)

        inorder(node=root, x=0)
        return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        val = 0
        node, stack = root, []
        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node.val = val = node.val + val
                node = node.left
        return root
