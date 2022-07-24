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


# Adding an iterative implementation
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        stack = [(root, 0)]
        while stack:
            node, val = stack.pop()
            if node:
                val += node.val
                if not node.left and not node.right and val == target:
                    return True

                if node.right:
                    stack.append((node.right, val))
                if node.left:
                    stack.append((node.left, val))

        return False


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:

        def dfs(node, x):
            # null node
            if not node:
                return False
            # leaf node
            elif not node.left and not node.right:
                return node.val == x
            else:
                return dfs(node.left, x-node.val) or dfs(node.right, x-node.val)

        return dfs(root, target)
