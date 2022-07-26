"""
103. Binary Tree Zigzag Level Order Traversal
Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS for level order traverse. 
        Alternate order of vals while storing it.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        if not root:
            return []

        res, queue = [], [root]
        flip = False

        while queue:
            vals, level = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            res.append(vals[::-1] if flip else vals)
            queue = level
            flip = not flip

        return res
