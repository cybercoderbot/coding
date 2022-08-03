"""
545. Boundary of Binary Tree
Medium

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.
Given the root of a binary tree, return the values of its boundary.
"""


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        The main idea is to carry the flag isleft and isight in the traverse()
        to help to decide when to add node values to the boundary array.
        """
        if not root:
            return []

        @lru_cache(None)
        def traverse(root, isleft, isright):
            if not root:
                return
            if (not root.left and not root.right) or isleft:
                res.append(root.val)

            if root.left and root.right:
                traverse(root.left, isleft, False)
                traverse(root.right, False, isright)
            else:
                traverse(root.left,  isleft, isright)
                traverse(root.right, isleft, isright)

            if (root.left or root.right) and isright:
                res.append(root.val)
            return

        res = [root.val]
        traverse(root.left, True, False)
        traverse(root.right, False, True)
        return res


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        left = []
        node = root.left
        while node:
            left.append(node.val)
            if node.left:
                node = node.left
            else:
                # if can't find a left node, try going to right
                node = node.right

        right = []
        node = root.right
        while node:
            right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        # trim last element because it is a leaf
        left = left[:-1]
        right = right[:-1]
        leaves = self.getLeaves(root)

        # don't forget to reverse right
        return [root.val] + left + leaves + right[::-1]

    def getLeaves(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return self.getLeaves(node.left) + self.getLeaves(node.right)
