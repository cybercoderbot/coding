"""
114. Flatten Binary Tree to Linked List
Medium

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

This solution is inspired by this thread (and a few other similar ones). The original solution is concise, efficient and reasonably easy to understand. The only shortcoming is that a global-ish variable is used. Below alternative implementation aims to overcome this weakness.

An inner function fn is defined to flatten the sub-tree rooted at node to a linked list. The input variable tail is to be added to the linked list. In this way, we can call fn twice

head = fn(node.right, tail) #returned head of linked list is to be used as tail in below call
head = fn(node.left, head)
node.right = head
node.left = None

This will organize the tree as the desired linked list. 
Below implementation is an even shorter summary of above thought.
"""


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node, tail):
            """Return head of flattened binary tree"""
            if not node:
                return tail

            left = node.left
            tail = dfs(node.right, tail)
            node.left = None
            node.right = dfs(left, tail)

            return node

        dfs(node=root, tail=None)

        return


class Solution:
    def flatten(self, root: TreeNode, tail=None) -> None:
        """
        Return head of flattened binary tree
        """
        if not root:
            return tail

        left = root.left
        root.left = None
        tail = self.flatten(root.right, tail)
        root.right = self.flatten(left, tail)

        return root


class Solution:
    """simple preorder traversal by recursion"""

    def dfs(self, root):
        if self.pre:
            self.pre.right = root
            self.pre.left = None

        self.pre = root
        right = root.right

        if root.left:
            self.dfs(root.left)
        if right:
            self.dfs(right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.pre = None
        self.dfs(root)


class Solution(object):
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        Non-recursive preorder traversal
        In the flattened tree, each node's right child points to the next node 
        of a pre-order traversal.
        """

        if not root:
            return None

        cur = TreeNode(None)
        stack = [root]

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            cur.right = node
            cur.left = None
            cur = node
