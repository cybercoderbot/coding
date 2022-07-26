"""
117. Populating Next Right Pointers in Each Node II
Medium


Given a binary tree

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 
Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        parent = root
        while parent:
            child = dummy = Node()
            while parent:
                if parent.left:
                    child.next = child = parent.left
                if parent.right:
                    child.next = child = parent.right
                parent = parent.next
            parent = dummy.next
        return root


"""
This can be solved via a typical BFS as below. 
After solving many LC problems, I tend to prefer general methods rather than the ad-hoc ones.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        BFS for level order traverse
        Connect nodes one by one in each level
        """

        if not root:
            return None

        queue = [root]
        while queue:
            level, prev = [], None
            for node in queue:
                node.next = prev
                prev = node

                if node.right:
                    level.append(node.right)
                if node.left:
                    level.append(node.left)
            queue = level

        return root


"""
Comparing to below solution for 116. Populating Next Right Pointers in Each Node, it is clear that info of perfect binary tree can somewhat simplify the implementation.

"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        116. Populating Next Right Pointers in Each Node
        The tree if perfect (left and right)

        Truly O(1) space
        O(1) space if not counting recursion stack
        """
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
