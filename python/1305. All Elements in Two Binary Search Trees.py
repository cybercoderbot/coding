"""
1305. All Elements in Two Binary Search Trees
Medium

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
"""


def getAllElements(self, root1, root2):
    """
    Before you scream "But sorting isn't linear!", know that it's →Timsort, which identifies the two already sorted runs as such and simply merges them. And since it's done in C, it's likely faster than if I tried merging myself in Python.
    """
    nums = []

    def inorder(root):
        if not root:
            return

        inorder(root.left)
        nums.append(root.val)
        inorder(root.right)
        return

    inorder(root1)
    inorder(root2)

    return sorted(nums)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Merge these two sorted arrays into one sorted array
        """

        def inorder(node):
            """
            Has to use a stack to store values
            """
            res, stack = [], []
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    res.append(node.val)
                    node = node.right
            return res

        nums1 = inorder(root1)
        nums2 = inorder(root2)
        M, N = len(nums1), len(nums2)

        res = []
        i = j = 0
        while i < M or j < N:
            if j == N or (i < M and nums1[i] < nums2[j]):
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        return res
