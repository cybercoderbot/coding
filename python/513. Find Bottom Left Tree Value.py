"""
513. Find Bottom Left Tree Value
Medium

Given the root of a binary tree, return the leftmost value in the last row of the tree. 

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        BFS tree traverse
        First node in last layer: leftmost value
        """
        lastRow = -1
        queue = collections.deque([(root, 0)])

        while queue:
            node, i = queue.popleft()
            if i > lastRow:
                res = node.val
                lastRow = i

            if node.left:
                queue.append((node.left, i+1))

            if node.right:
                queue.append((node.right, i+1))

        return res
