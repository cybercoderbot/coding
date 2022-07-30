"""
518. Coin Change 2
Medium

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Bottom up DP
        Time: O(M*N), Space: O(N)
        """
        dp = [1] + [0] * amount
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
        return dp[-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for x in range(amount-coin+1):
                dp[x+coin] += dp[x]
        return dp[-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Top down DP
        Time: O(M*N), Space: O(N)
        """
        coins.sort(reverse=True)
        N = len(coins)

        @lru_cache(None)
        def dp(i, target):
            """Return number of combo in coins[i:] to make up target"""
            nonlocal N
            if target < 0:
                return 0
            if target == 0:
                return 1

            return sum(dp(k, target-coins[k]) for k in range(i, N))

        return dp(i=0, target=amount)
