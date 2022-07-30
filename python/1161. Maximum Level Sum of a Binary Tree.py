"""
1161. Maximum Level Sum of a Binary Tree
Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
    """
    Traverse the tree by level and collect sum of each level.

    Time: O(N)
    Space: O(N)
    """
    res = level = 0
    maxsum = -inf
    queue = [root]
    while queue:
        level += 1
        queue2 = []
        levelsum = 0
        for node in queue:
            levelsum += node.val
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        if levelsum > maxsum:
            res = level
            maxsum = levelsum
        queue = queue2

    return res
