"""
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.maxDepth(root.right) + 1
        if not root.right:
            return self.maxDepth(root.left) + 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Iterative DFS
        This is just to traverse the tree and find deepest node.
        """
        if not root:
            return 0

        queue = [(root, 1)]
        res = 0
        while queue:
            node, depth = queue.pop()
            res = max(res, depth)

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        BFS by level
        """
        if not root:
            return 0

        depth, queue = 0, [root]
        while queue:
            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
            depth += 1
        return depth
