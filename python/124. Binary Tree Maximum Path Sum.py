"""
124. Binary Tree Maximum Path Sum
Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Algorithm:
        Traverse the tree and retrieve each node's max path sum of left and right node. 
        Compute the max path sum pass the current node and store it in ans.

        Time complexity O(N) 
        Space complexity O(N)
        """

        def traverse(node):
            """Returns max path starting at node"""
            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)

            res.append(left + node.val + right)

            return max(left, right) + node.val

        res = []
        traverse(root)

        return max(res)


# There are a few tricks to save the space usage:
# use a instance variable self.ans;
# use a list ans = [];
# use a nonlocal variable.


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # res: max path starting at root
        self.res = -inf

        def traverse(node):
            """Returns max path starting at node"""
            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            self.res = max(self.res, left + node.val + right)

            return max(left, right) + node.val

        traverse(root)
        return self.res


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # res: max path starting at root
        res = [-inf]

        def traverse(node):
            """Returns max path starting at node"""
            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            res[0] = max(res[0], left + node.val + right)

            return max(left, right) + node.val

        traverse(root)

        return res[0]


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # res: max path starting at root
        res = -inf

        def traverse(node):
            """Returns max path starting at node"""
            nonlocal res
            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            res = max(res, left + node.val + right)

            return max(left, right) + node.val

        traverse(root)

        return res
