"""
783. Minimum Distance Between BST Nodes
Easy


Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""


"""
Since it is a binary search tree, inorder depth-first traversal would visit the nodes whose values are in ascending order. 
As a result, the minimum distance can only occur between the two nodes visited in sequence. Here, two implementations 
are presented:

iterative implementation using a stack
recursive implementation(leveraging on call stack).


Classical inorder traverse. Time complexity O(N). Space complexity O(h)

This question is the same as problem 530.Minimum Absolute Difference in BST. Except that in 530th, we are given a binary search tree with non-negative values.
However, it seems that it doesn't have any negative case and my solution in cpp get accepted.


"""


class Solution(object):
    pre, res = -inf, inf

    def minDiffInBST(self, root):

        if root.left:
            self.minDiffInBST(root.left)

        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.res


"""
At each node, keep track of the highest and lowest possible values. 
When we've passed the leaf node, check the difference. 
Bubble the minimum difference up the tree.
"""


class Solution(object):
    def minDiffInBST(self, root):

        def traverse(node, low, high):
            if not node:
                return high - low

            left = traverse(node.left, low, node.val)
            right = traverse(node.right, node.val, high)

            return min(left, right)

        return traverse(root, -inf, inf)
