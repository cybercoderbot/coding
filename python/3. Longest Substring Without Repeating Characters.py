"""
3. Longest Substring Without Repeating Characters
Medium

26486

1150

Add to List

Share
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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 解题思路：Sliding window
        # 变量left和right分别记录子串的起点和终点
        # 字典count存储当前子串中各字符的个数
        # 从左向右逐字符遍历原始字符串，每次将right + 1
        # 当新增字符c的计数 > 1时，向右移动起点left，并将s[left]在字典中的计数-1，直到count[c]<=1为止
        # 更新最大长度

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
