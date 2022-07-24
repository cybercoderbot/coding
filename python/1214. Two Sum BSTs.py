"""
1214. Two Sum BSTs
Medium

Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
"""


def inorder(node):
    """Return inorder traversal of binary tree."""
    res, stack = [], []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """
        Inorder traverse the two binary search trees and collect their values in two
        arrays (sorted in ascending order). Search for target with 2-pointer approach.
        Time complexity O(M+N)
        Space complexity O(M+N)
        """

        tree1 = inorder(root1)
        tree2 = inorder(root2)

        M, N = len(tree1), len(tree2)
        low, high = 0, N-1

        while low < M and high >= 0:

            if tree1[low] + tree2[high] == target:
                return True
            elif tree1[low] + tree2[high] < target:
                low += 1
            else:
                high -= 1

        return False
