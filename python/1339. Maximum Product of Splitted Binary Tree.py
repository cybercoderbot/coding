"""
1339. Maximum Product of Splitted Binary Tree
Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. 
Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.
Their product is 90 (15*6)
"""


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Postorder traverse of the tree
        """
        @lru_cache(None)
        def sumOfNodes(node):
            """Return sum of subtree."""
            if not node:
                return 0
            left = sumOfNodes(node.left)
            right = sumOfNodes(node.right)
            res = node.val + left + right
            nums.append(res)
            return res

        nums = []
        total = sumOfNodes(root)
        products = [x * ((total-x)) for x in nums]
        return max(products) % 1_000_000_007
