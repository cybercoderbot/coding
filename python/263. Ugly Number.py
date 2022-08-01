"""
263. Ugly Number
Easy

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Loop through factors 2, 3 and 5, and check if num can be divided by the factor.
        If a number is ugly, then it will reach 1 eventually.
        """
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        264. Ugly Number II. Return the nth ugly number.
        ugly(n) = min(x * ugly(n//x) for x in (2, 3, 5))
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
