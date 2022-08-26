"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:

        res, left = 0, 0
        freq = collections.Counter()
        for right, c in enumerate(s):
            freq[c] += 1
            while any(freq[x] > 1 for x in freq.keys()):
                freq[s[left]] -= 1
                left += 1
            res = max(res, right-left + 1)
        return res
