"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

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
        Compare otehrs against it
        """
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest
