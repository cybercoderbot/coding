"""
298. Binary Tree Longest Consecutive Sequence
Medium

Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

Example 1:
Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        Traverse the tree and keep track of lcs.
        Iterative BFS using queue
        Time: O(N), Space: O(N)
        """
        if not root:
            return 0

        res = 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, cur = queue.popleft()
            res = max(res, cur)
            for child in node.left, node.right:
                if child:
                    nxt = cur + 1 if child.val == node.val+1 else 1
                    queue.append((child, nxt))
        return res


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        Traverse the tree and keep track of lcs.
        Iterative DFS using stack
        Time: O(N), Space: O(N)
        """
        if not root:
            return 0

        res = 0
        stack = [(root, 1)]
        while stack:
            node, cur = stack.pop()
            res = max(res, cur)
            for child in node.left, node.right:
                if child:
                    nxt = cur + 1 if child.val == node.val+1 else 1
                    stack.append((child, nxt))
        return res
