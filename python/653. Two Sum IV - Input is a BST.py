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
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if k - node.val in seen:
                return True

            seen.add(node.val)
            queue.append(node.right)
            queue.append(node.left)

        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if k - node.val in seen:
                return True

            seen.add(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return False
