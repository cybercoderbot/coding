"""
96. Unique Binary Search Trees
Medium

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Dynamic programming
Given n numbers, we can scan through them. 
At any point, say i, 1~i becomes left subtree, 
i becomes root and i+1~n becomes right subtree. 
As a result, if we define dp(n) as the number of such trees when there are n nodes, 
then

dp(n) = dp(0)*dp(n-1) + dp(1)*dp(n-2) + ... + dp(n-1)*dp(0)

which represents when 1, 2, ..., n are the roots respectively.
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]
