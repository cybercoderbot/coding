"""
1602. Find Nearest Right Node in Binary Tree
Medium

Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.



Example 1:
Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.

Example 2:
Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.


Traverse the tree and return the node to the right of u.
"""


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        """
        BFS by level
        - Time complexity O(N)
        - Space complexity O(N)

        """
       if not root:
            return []

        queue = [root]
        while queue:
            prev = None
            level = []
            for node in queue:
                if not node:
                    continue
                if node == u:
                    return prev
                prev = node
                level.append(node.right)
                level.append(node.left)
            queue = level


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        """
        BFS by index
        - Time complexity O(N)
        - Space complexity O(N)
        """

        d0 = -1
        queue = [(root, 0)]
        for node, depth in queue:

            if d0 != depth:
                d0, prev = depth, None

            if node == u:
                return prev
            prev = node

            if node.right:
                queue.append((node.right, depth+1))
            if node.left:
                queue.append((node.left, depth+1))


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        """
        Pre-order DFS by index
        - Time complexity O(N)
        - Space complexity O(N)
        """

       seen = {}
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node == u:
                return seen.get(depth, [None])[-1]
            seen.setdefault(depth, []).append(node)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))

