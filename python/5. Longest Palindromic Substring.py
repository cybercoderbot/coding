"""
5. Longest Palindromic Substring
Medium

Share
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
        for i in range(len(s)):
            odd = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res

    def palindromeAt(self, s, left, right):
        # starting at left, right expand outwards to find the biggest palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1: right]
