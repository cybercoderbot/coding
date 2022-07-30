"""
522. Longest Uncommon Subsequence II
Medium

Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string). 

Example 1:
Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:
Input: strs = ["aaa","aaa","aa"]
Output: -1
"""


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(s, t):
            """Return True if s is t subsequence of s."""
            t = iter(t)
            return all(c in t for c in s)

        sort = sorted(strs, key=len, reverse=True)
        for s in sort:
            if sum(isSub(s, t) for t in strs) == 1:
                return len(s)
        return -1


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def isSub(p, s):
            """Return True if p is a subsequence of s."""
            s = iter(s)
            return all(c in s for c in p)

        res = -1
        for i, s in enumerate(strs):
            for j in range(len(strs)):
                if i != j and len(s) <= len(strs[j]) and isSub(s, strs[j]):
                    break
            else:
                res = max(res, len(s))
        return res
