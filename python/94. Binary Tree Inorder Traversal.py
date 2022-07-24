"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]


Example 2:
Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res


def inorder(node, res):
    if not node:
        return
    inorder(node.left, res)
    res.append(node.val)
    inorder(node.right, res)


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        inorder(root, res)
        return res
