"""
1038. Binary Search Tree to Greater Sum Tree
Medium

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]
"""


class Solution:
    pre = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        We need to do the work from biggest to smallest, right to left.
        pre records the previous value the we get, the total sum of bigger values.
        For each node, we update root.val with root.val + pre.
        Time O(N), Space O(height)
        """
        if root.right:
            self.bstToGst(root.right)

        self.pre += root.val
        root.val = self.pre

        if root.left:
            self.bstToGst(root.left)

        return root


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def reversedInorder(node: TreeNode, pre: int) -> int:
            if not node:
                return pre
            node.val += reversedInorder(node.right, pre)
            res = reversedInorder(node.left, node.val)
            return res

        reversedInorder(node=root, pre=0)
        return root
