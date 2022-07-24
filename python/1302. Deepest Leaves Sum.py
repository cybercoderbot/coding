"""
1302. Deepest Leaves Sum
Medium

Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        Level-order traverse the tree and keep track of sum at each level.

        Time complexity O(N)
        Space complexity O(1)
        """
        if not root:
            return 0

        queue = [root]
        while queue:
            res, level = 0, []
            for node in queue:
                res += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level

        return res
