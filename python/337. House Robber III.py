"""
337. House Robber III
Medium

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

"""
# Traverse the tree starting from the node. At every node, keep track of two numbers,

# maximum money if the current house is robbed;
# maximum money if the current house is skipped.
# Implementation


class Solution:
    def rob(self, root: TreeNode) -> int:

        def helper(node):
            """return [rob, skip]"""
            if not node:
                return 0, 0

            left = helper(node.left)
            right = helper(node.right)

            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not

            skip = max(left) + max(right)

            return rob, skip

        return max(helper(root))
