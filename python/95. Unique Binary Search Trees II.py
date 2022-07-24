"""
95. Unique Binary Search Trees II
Medium


Share
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
"""


"""
Define functions fn(low, high) to return the trees using numbers between low (inclusive) 
and hi (exclusive). In this way, the trees can be built recursively. For example, at node i, 
its left subtree can be built from fn(lo, i) and its right subtree can be built from fn(i+1, hi).

"""


"""
[Python] DFS with Memoization - Clean & Concise
107
hiepit's avatar
hiepit

34438
Last Edit: September 2, 2021 2:34 AM

4.3K VIEWS

Idea

Let dfs(left, right) return all valid BSTs where values in the BST in range [left..right].
Then dfs(1, n) is our result.
To solve dfs(left, right), we just
Generate root value in range [left...right]
Get left subtrees by leftNodes = dfs(left, root-1)
Get right subtrees by rightNodes = dfs(root+1, right).
Add all combination between leftNodes and rightNodes to form root trees.
Can we cache the result of dfs(left, right) to prevent it to re-compute multiple time.
There is a simillar problem, which is 894. All Possible Full Binary Trees, try to solve it yourself.

Complexity

Time: O(C0+C1+...Cn), where Cn is the Catalan number, n <= 8. Can check this problem 96. Unique Binary Search Trees to know why the number of nodes in the BST with n nodes is a Catalan number.
The Catalan numbers for n = 0, 1, 2, 3, 4, 5, 6, 7, 8 are 1, 1, 2, 5, 14, 42, 132, 429, 1430.
Space: O(n * Cn), there is total Cn BSTs, each BST has n nodes.
"""


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @lru_cache(None)
        def dfs(left, right):

            if left > right:
                return [None]

            if left == right:
                return [TreeNode(left)]

            res = []
            for rval in range(left, right+1):
                leftNodes = dfs(left, rval - 1)
                rightNodes = dfs(rval+1, right)

                for left in leftNodes:
                    for right in rightNodes:
                        node = TreeNode(rval, left, right)
                        res.append(node)
            return res

        return dfs(1, n)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        @lru_cache(None)
        def dfs(low, high):
            """Return root of tree using nums from low (inclusive) to high (exclusive)"""
            if low == high:
                return [None]

            res = []
            for node in range(low, high):
                for left in dfs(low, node):
                    for right in dfs(node+1, high):
                        res.append(TreeNode(node, left, right))

            return res

        return dfs(1, n+1)
