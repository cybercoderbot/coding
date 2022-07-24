"""
156. Binary Tree Upside Down
Medium

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.


Example 1:
Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]

Example 2:
Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:
            return root

        res = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None

        return res


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        def rotated(node):
            """Return root of rotated tree."""
            if not node.left:
                return node
            res = rotated(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = node.right = None
            return res

        return rotated(root)
