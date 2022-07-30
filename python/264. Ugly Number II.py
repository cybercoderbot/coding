"""
264. Ugly Number II
Medium

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number. 

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Bottom-up DP
        """

        dp = [1]
        i = j = k = 0

        for _ in range(n-1):
            x = min(2 * dp[i], 3 * dp[j], 5 * dp[k])
            dp.append(x)
            if 2 * dp[i] == x:
                i += 1
            if 3 * dp[j] == x:
                j += 1
            if 5 * dp[k] == x:
                k += 1
        return dp[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        An interesting fact about ugly number sequence is that it is possible to 
        figure out the next ugly number given an ugly number.

        Define fn(x) to return next ugly number given an ugly number x through

        fn(x) = min(f*fn(x//f) for f in (2, 3, 5)).

        top-down DP
        """

        @lru_cache(None)
        def fn(k):
            """Return the smallest ugly number larger than k (not necessarily ugly)."""
            if k == 0:
                return 1
            return min(x * fn(k//x) for x in (2, 3, 5))

        res = 1
        for _ in range(n-1):
            res = fn(res)
        return res
