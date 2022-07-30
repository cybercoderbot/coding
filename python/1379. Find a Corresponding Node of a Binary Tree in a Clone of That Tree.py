"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
Easy

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Example 2:
Input: tree = [7], target =  7
Output: 7

Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Preorder treverse the tree
        Keep a pair of (src, dst) in the queue
        Constantly check if src == target.
        If yes, return dst
        """
        queue = [(original, cloned)]
        while queue:
            src, dst = queue.pop(0)
            if src == target:
                return dst
            if src:
                queue.append((src.left, dst.left))
                queue.append((src.right, dst.right))
        return None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        if not original or not cloned:
            return None

        if original == target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)
        right = self.getTargetCopy(original.right, cloned.right, target)

        return left or right
