"""
272. Closest Binary Search Tree Value II
Hard

Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.


Example 1:
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]

Example 2:
Input: root = [1], target = 0.000000, k = 1
Output: [1]
"""


def inorder(node: TreeNode):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def preorder(node: TreeNode):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def postorder(node: TreeNode):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        nums = inorder(root)
        # nums = preorder(root)
        # nums = postorder(root)
        nums.sort(key=lambda x: abs(x - target))

        return nums[:k]
