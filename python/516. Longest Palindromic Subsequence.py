"""
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(None)
        def dp(i, j):
            """Palindrom subseq s[i:j]"""
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return palinBetween(i+1, j-1) + 2
            return max(dp(i, j-1), dp(i+1, j))

        return dp(i=0, j=len(s)-1)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
