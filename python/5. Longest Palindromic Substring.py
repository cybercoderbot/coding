"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        odd, even = "", ""
        for i in range(len(s)):
            odd = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res

    def palindromeAt(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
