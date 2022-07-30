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

        res = left = right = 0
        count = {}
        for c in s:
            right += 1
            count[c] = count.get(c, 0) + 1
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left)
        return res
