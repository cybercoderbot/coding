"""
968. Binary Tree Cameras
Hard

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
"""


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
    """
    Greedy - tri-color encoding
    """
       def cover(node):
            """Return color-coding of a node.
            0 - not covered
            1 - covered w/o camera
            2 - covered w/ camera
            """
            nonlocal res
            if not node:
                return 1
            left = cover(node.left)
            right = cover(node.right)
            if left == 0 or right == 0:
                res += 1
                return 2  # add a camera
            if left == 2 or right == 2:
                return 1
            return 0

        res = 0
        return int(cover(root) == 0) + res
