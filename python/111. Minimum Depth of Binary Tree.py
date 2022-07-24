"""
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [(root, 1)]
        for node, depth in queue:
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth, queue = 1, [root]
        while queue:
            level = []
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
            depth += 1

        return depth
