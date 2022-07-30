"""
257. Binary Tree Paths
Easy

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        We initiate the stack by a root node and then at each step we pop out one node and its path. 
        If the poped node is a leaf, one update the list of all paths. 
        If not, one pushes its child nodes and corresponding paths into stack until all nodes are checked.


        Complexity Analysis
        - Time complexity : O(N) since each node is visited exactly once.
        - Space complexity : O(N) as we could keep up to the entire tree.

        """

        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths
