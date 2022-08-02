"""
1161. Maximum Level Sum of a Binary Tree
Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, 
and so on. Return the smallest level x such that the sum of all the values of nodes at level 
x is maximal.

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
        levels = defaultdict(int)

        def traverse(root, depth):
            if not root:
                return
            levels[depth] += root.val
            traverse(root.left,  depth+1)
            traverse(root.right, depth+1)
            return

        traverse(root, 1)
        return max(levels, key=lambda x: levels[x])
        # return max(levels, key=levels.get)


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res, queue, height = [-inf, -1], [root], 1
        while queue:
            res = max(res, [sum(node.val for node in queue), -height])
            queue = [c for node in queue for c in (node.left, node.right) if c]
            height += 1
        return -res[1]


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        Traverse the tree by level and collect sum of each level.
        Time: O(N), Space: O(N)
        """
        if not root:
            return 0

        res = depth = 0
        high = -inf

        queue = [root]
        while queue:
            depth += 1
            level, queue2 = 0, []
            for node in queue:
                level += node.val
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            if level > high:
                res = depth
                high = level
            queue = queue2

        return res
