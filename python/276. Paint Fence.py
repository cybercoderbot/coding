"""
276. Paint Fence
Medium

You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.

Example 1:
Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.

Example 2:
Input: n = 1, k = 1
Output: 1
Example 3:

Input: n = 7, k = 2
Output: 42
"""


"""
Number of ways to paint 1 fence with k color = k
Number of ways to paint 2 fence with k color = k * k (2 Adjacenct fence can be same color)
Number of ways to paint 3 fence with k color - there are two posibilities

Fence 1 and Fence 2 are different colors = k * (k-1) * k
Fence 1 and Fence 2 are same colors = k * 1 * (k - 1) - Fence 2 is set 1 once becuase we can chose only 1 color . Fence 3 is k-1 because we cannot choose the color chosen for fence 2 and 3
Generalising the above step

If f(n) is number of ways to paint n fences with k color
f(3) = k * (k-1) * k + k * 1 * (k -1) = (k-1) (k + k * k)
f(3) = (k-1) (f(1) + f(2))
This implies f(n) = (k-1) (f(n-1) +f(n-2))
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n * k == 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = k
        dp[1] = k * k

        for i in range(2, n):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])

        return dp[n-1]
