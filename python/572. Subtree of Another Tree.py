"""
572. Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""


"""
# Naive approach, O(|s| * |t|)
# For each node of s, let's check if it's subtree equals t.
We can do that in a straightforward way by an isMatch function:
check if s and t match at the values of their roots, plus their subtrees match.
Then, in our main function, we want to check if s and t match, or if t is a subtree
of a child of s.

"""


class Solution:
   def isMatch(self, s, t):
        if not (s and t):
            return s == t

        left = self.isMatch(s.left, t.left)
        right = self.isMatch(s.right, t.right)
        return s.val == t.val and left and right


    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        if not s:
            return False
        if self.isMatch(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
