"""
113. Path Sum II
Medium

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        """
        Record each node's parent {node: parent} while traversing the tree
        Use a queue to store (node, pre) pair
        When reach to leaf, get leaf->root path
        Reverse path, get root->leaf path
        """
        if not root:
            return []

        res = []
        parent = {root: None}
        queue = [(root, 0)]
        while queue:
            node, pre = queue.pop(0)
            pre += node.val

            if node.left:
                parent[node.left] = node
                queue.append((node.left, pre))
            if node.right:
                parent[node.right] = node
                queue.append((node.right, pre))

            if not node.left and not node.right and pre == target:
                path = []
                while node:
                    path.append(node.val)
                    node = parent[node]
                res.append(path[::-1])

        return res
