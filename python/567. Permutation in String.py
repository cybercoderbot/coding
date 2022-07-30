"""
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


One string is a permutation of another if the two strings have the same character frequencies
Hence:
find freq dict for s1
find freq dict for substrings of s2 (that are the same size as s1)
runtime: O(n*k)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1, s2 are permutations: Counter(s1) == Counter(s2)
        Time: O(K*N)
        """

        d1 = collections.Counter(s1)
        K, N = len(s1), len(s2)
        for i in range(N-K+1):
            d2 = Counter(s2[i:i+K])
            if d1 == d2:
                return True
        return False
