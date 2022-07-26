"""
230. Kth Smallest Element in a BST
Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Inorder traverse: nums sorted in ascending order
        """

        def inorder(node):
            """inorder traverse to collect nums"""
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        nums = []
        inorder(root)

        return nums[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        stack = []

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
