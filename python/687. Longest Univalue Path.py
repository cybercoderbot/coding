"""
687. Longest Univalue Path
Medium

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).

Example 2:
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def univalLength(node, parent):
            nonlocal res
            if not node:
                return 0

            left = univalLength(node.left, node.val)
            right = univalLength(node.right, node.val)
            res = max(res, left + right)

            if node.val != parent:
                return 0
            else:
                return max(left, right) + 1

        univalLength(root, None)
        return res
