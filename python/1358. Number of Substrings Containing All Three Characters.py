"""
1358. Number of Substrings Containing All Three Characters
Medium

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, res = [-1]*3, 0
        for i, x in enumerate(s):
            a[ord(x)-ord('a')] = i
            res += min(a)+1
        return res
