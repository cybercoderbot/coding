"""
1382. Balance a Binary Search Tree
Medium

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:
Input: root = [2,1,3]
Output: [2,1,3]
"""


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Traverse binary tree in-order to get sorted array
        The problem become 108. Convert Sorted Array to Binary Search Tree
        """
        @lru_cache(None)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
            return

        def build(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build(nums[:mid])
            root.right = build(nums[mid + 1:])
            return root

        nums = []
        inorder(root)
        return build(nums)
