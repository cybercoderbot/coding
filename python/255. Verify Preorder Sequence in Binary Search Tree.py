"""
255. Verify Preorder Sequence in Binary Search Tree
Medium

Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.


Example 1:
Input: preorder = [5,2,1,3,6]
Output: true

Example 2:
Input: preorder = [5,2,6,1,3]
Output: false
"""


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        Following what's given in preorder, we can reconstruct the BST 
        and check if it violates symmetric order.
        - Time complexity O(N)
        - Space complexity O(N)
        """

        low = -inf
        stack = [inf]

        for x in preorder:
            if x < low:
                return False

            while stack and x > stack[-1]:
                low = stack.pop()

            stack.append(x)

        return True
