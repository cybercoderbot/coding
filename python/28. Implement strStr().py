"""
28. Implement strStr()
Easy

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time: O(N * M).
        Checking haystack[i:i+N] == needle is O(N), done O(M) times.
        """
        M, N = len(haystack), len(needle)
        for i in range(M-N+1):
            if haystack[i:i+N] == needle:
                return i
        return -1
