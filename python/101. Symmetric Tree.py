"""
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isReflective(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return isReflective(t1.left, t2.right) and isReflective(t1.right, t2.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return isReflective(root, root)
