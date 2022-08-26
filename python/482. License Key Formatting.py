"""
482. License Key Formatting
Easy

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        O(N) time, O(N) space
        """
        s = s.replace("-", "").upper()[::-1]
        return '-'.join(s[i:i+k] for i in range(0, len(s), k))[::-1]


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Add # to make the length is a multiple of k. Then remove it.
        """
        s = s.replace('-', '').upper()
        if len(s) % k:
            m = k - len(s) % k
            s = '#' * m + s
        idx = range(0, len(s), k)
        tmp = [s[i:i+k] for i in idx]
        return '-'.join(tmp).replace('#', '')
