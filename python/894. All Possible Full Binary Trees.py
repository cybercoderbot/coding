"""
894. All Possible Full Binary Trees
Medium

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
[Python3] memoized recursion

Creat full binary trees recursively.

Time complexity O(2^N)
Space complexity O(2^N)
"""


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:

        @lru_cache(None)
        def recurse(n):
            """Return all full binary trees of n nodes."""
            if n == 1:
                return [TreeNode()]

            res = []
            for i in range(1, n, 2):
                for left in recurse(i):
                    for right in recurse(n-1-i):
                        res.append(TreeNode(left=left, right=right))
            return res

        return recurse(N)
