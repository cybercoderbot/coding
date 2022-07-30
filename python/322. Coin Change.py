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
        def dp(i):
            """Return number of combo in coins[i:] to make up amount"""
            nonlocal N
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            return sum(dp(k, amount-coins[k]) for k in range(i, N))

        return dp(i=0)
