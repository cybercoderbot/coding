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


class Solution:
    def isSymmetric(self, root):
        """Iterative Solution"""

        if root is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False

        return True


class Solution:
    def isReflective(self, root: Optional[TreeNode]) -> bool:

        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        left = self.isReflective(t1.left, t2.right)
        right = self.isReflective(t1.right, t2.left)

        return t1.val == t2.val and left and right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Recursive Solution"""
        return self.isReflective(root, root)
