"""
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].


Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        res, queue = [], [root]
        while queue:
            valsum, level = 0, []
            for i, node in enumerate(queue):
                valsum += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            res.append(valsum/(i+1))
            queue = level

        return res


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            vals = []
            level = []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if vals:
                res.append(sum(vals)/len(vals))
            queue = level

        return res


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if not root:
            return []

        res, queue = [], [root]

        while queue:
            vals, level = [], []
            for node in queue:
                if node:
                    vals.append(node.val)
                    level.append(node.left)
                    level.append(node.right)
            if vals:
                res.append(sum(vals)/len(vals))
            queue = level

        return res
