"""
116. Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
"""

# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = [root]
        while queue:
            level, tail = [], None
            for node in queue:
                node.next = tail
                tail = node
                if node.right:
                    level.append(node.right)
                if node.left:
                    level.append(node.left)
            queue = level
        return root


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """O(logN) space"""

        if not root:
            return None

        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Truly O(1) space
        O(1) space if not counting recursion stack
        """
        if not root:
            return None

        node = root
        while node and node.left:
            p = node
            while p:
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left
                p = p.next
            node = node.left

        return root
