"""
14. Longest Common Prefix
Easy

Find the longest common prefix string amongst an array of strings.
If no common prefix, return "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the word with minimum length
        Compare all the strings with it
        """
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]
        return shortest
