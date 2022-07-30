"""
161. One Edit Distance
Medium

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        Find the first diff between s and t and compare the rest for one of three cases.
        """

        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]

        return True


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        Find the first diff between s and t and compare the rest for one of three cases.
        """
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        i = 0
        while i < min(len(t), len(s)):
            if s[i] != t[i]:
                break
            i += 1

        return s[i:] == t[i+1:] or s[i+1:] == t[i+1:] or s[i+1:] == t[i:]
