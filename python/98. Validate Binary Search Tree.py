"""
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        In-order traversal(recursive)
        """

        def inorder(node):
            """Collect value on bst"""
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)

        return all(res[i-1] < res[i] for i in range(1, len(res)))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        In-order traversal (iterative=> early termination)
        """

        node, stack = root, []
        prev = -inf

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev >= node.val:
                    return False
                prev = node.val
                node = node.right

        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Pre-order traversal
        """

        def preorder(node, low, high):
            """Return True if tree rooted at node is a valid BST bounded between lo and hi"""
            if not node:
                return True
            left = preorder(node.left, low, node.val)
            right = preorder(node.right, node.val, high)
            return low < node.val < high and left and right

        return preorder(root, -inf, inf)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Iterative pre-order traversal
        """

        stack = [(root, -inf, inf)]
        while stack:
            node, low, high = stack.pop()
            if low < node.val < high:
                if node.left:
                    stack.append((node.left, low, node.val))
                if node.right:
                    stack.append((node.right, node.val, high))
            else:
                return False

        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Post-order traverse
        """

        if not root:
            return True

        def postorder(node):
            """Return True if tree rooted at node is a valid bst and its span"""
            if node.left:
                valid1, low1, high1 = postorder(node.left)
            else:
                valid1, low1, high1 = True, node.val, -inf

            if node.right:
                valid2, low2, high2 = postorder(node.right)
            else:
                valid2, low2, high2 = True, inf, node.val

            valid = valid1 and valid2 and high1 < node.val < low2

            return valid, low1, high2

        res, _, _ = postorder(root)

        return res
