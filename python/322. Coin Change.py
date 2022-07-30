"""
322. Coin Change
Medium

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom-up DP

        Assume dp[i] is the fewest number of coins making up amount i, 
        then for every coin in coins, dp[i] = min(dp[i - coin] + 1).

        Time: is O(N * M), M = number of coins
        Space complexity is O(N), N = amount

        """

        dp = [0] + [inf] * amount

        for x in range(1, amount+1):
            for coin in coins:
                if coin <= x:
                    dp[x] = min(dp[x], 1 + dp[x-coin])

        return dp[-1] if dp[-1] < inf else -1


class Solution(object):

    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        """
        Bottom-up DP
        """

        dp = [0] + [inf for i in range(amount)]

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[-1] if dp[-1] < inf else -1
