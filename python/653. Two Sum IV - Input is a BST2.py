"""
653. Two Sum IV - Input is a BST
Easy

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

"""


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if k - node.val in seen:
                return True
            seen.add(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False
