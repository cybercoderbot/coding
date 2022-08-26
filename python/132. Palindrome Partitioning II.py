"""
132. Palindrome Partitioning II
Hard

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1
"""


class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        N = len(s)
        for i in range(1, N):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        dp = [inf] * (N+1)
        dp[0] = -1
        for i in range(N):
            for j in range(i, N):
                if s[i:j+1] == s[i:j+1][::-1]:
                    dp[j+1] = min(dp[j+1], dp[i]+1)
        return dp[-1]


class Solution:
    def minCut(self, s: str) -> int:
        """
        Let isPalindrome(l, r) be True if string s[l...r] is palindrome else False.
        Let dp(i) denote the minimum number of palindrome substrings of string s[i..n-1].
        The answer is dp(0) - 1 which is number minimum cuts need to be made on string s[0..n-1].
        """
        N = len(s)

        @lru_cache(None)
        def isPalindrome(i, j):
            """i,j inclusive"""
            if i == j:
                return True
            if s[i] != s[j]:
                return False
            return isPalindrome(i+1, j-1)

        @lru_cache(None)
        def dp(i):
            """True if s[i:]"""
            if i == N:
                return 0
            res = inf
            for j in range(i, N):
                if isPalindrome(i, j):
                    res = min(res, dp(j+1) + 1)
            return res

        return dp(i=0) - 1
