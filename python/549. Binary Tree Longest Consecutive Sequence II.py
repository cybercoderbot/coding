"""
549. Binary Tree Longest Consecutive Sequence II
Medium

Given the root of a binary tree, return the length of the longest consecutive path in the tree.
A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:
Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
"""


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        @lru_cache(None)
        def traverse(node):
            """
            Post-order traverse tree
            Return longest inc & dec seqs starting at node
            """
            nonlocal res
            if not node:
                return 0, 0

            inc1, dec1 = traverse(node.left)
            inc2, dec2 = traverse(node.right)
            inc = dec = 1
            if node.left:
                if node.left.val + 1 == node.val:
                    inc = inc1 + 1
                elif node.left.val - 1 == node.val:
                    dec = dec1 + 1
            if node.right:
                if node.right.val + 1 == node.val:
                    inc = max(inc, inc2 + 1)
                elif node.right.val - 1 == node.val:
                    dec = max(dec, dec2 + 1)

            res = max(res, inc + dec - 1)
            return inc, dec

        res = 0
        traverse(root)
        return res
