"""
266. Palindrome Permutation
Easy

Given a string s, return true if a permutation of the string could form a palindrome.

Example 1:
Input: s = "code"
Output: false

Example 2:
Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        counts = collections.Counter(s).items()
        return len([k for k, v in counts if v % 2]) <= 1
