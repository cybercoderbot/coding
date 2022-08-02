"""
112. Path Sum
Easy

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        """
        112. Path Sum. Return True if the tree has a root-to-leaf path
        Use a queue to store (node, pre) pair while traversing the tree
        """
        if not root:
            return False
        queue = [(root, 0)]
        while queue:
            node, pre = queue.pop(0)
            pre += node.val
            if not node.left and not node.right and pre == target:
                return True
            if node.left:
                queue.append((node.left, pre))
            if node.right:
                queue.append((node.right, pre))

        return False


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        """
        113. Path Sum II. Return all root-to-leaf paths summing to target.
        Record each node's parent {node: parent} while traversing the tree
        Use a queue to store (node, pre) pair
        When reach to leaf, get leaf->root path
        Reverse path, get root->leaf path
        """
        if not root:
            return []

        res = []
        parent = {root: None}
        queue = [(root, 0)]
        while queue:
            node, pre = queue.pop(0)
            pre += node.val

            if node.left:
                parent[node.left] = node
                queue.append((node.left, pre))
            if node.right:
                parent[node.right] = node
                queue.append((node.right, pre))

            if not node.left and not node.right and pre == target:
                path = []
                while node:
                    path.append(node.val)
                    node = parent[node]
                res.append(path[::-1])

        return res


class Solution:
    @lru_cache(None)
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        """
        Recursion
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target
        left = self.hasPathSum(root.left, target-root.val)
        right = self.hasPathSum(root.right, target-root.val)
        return left or right
