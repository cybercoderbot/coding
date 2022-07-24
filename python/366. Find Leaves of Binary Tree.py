"""
366. Find Leaves of Binary Tree
Medium

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
"""


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        Traverse the tree depth-first in post order and collect the values at the same height (from the leaf).

        Analysis
        Time complexity O(N)
        Space complexity O(N)
        """

        def traverse(node):
            """Return height of give node."""
            if not node:
                return 0
            height = max(traverse(node.left), traverse(node.right)) + 1
            seen[height].append(node.val)
            return height

        seen = defaultdict(list)
        traverse(root)

        return seen.values()
