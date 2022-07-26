"""
139. Word Break
Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
"""


"""
The idea is the following:

d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        M = len(s)
        dp = [False] * M
        for i in range(M):
            for w in wordDict:
                N = len(w)
                if w == s[i-N+1:i+1] and (dp[i-N] or i+1 == N):
                    dp[i] = True
        return dp[-1]


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 解题思路：
        # BFS（广度优先搜索）
        # 将当前单词拆分为前后两半，若前缀可以在字典dict中找到，则将后缀加入队列。

        # if s in wordDict: return True

        queue = [s]
        while queue:
            front = queue.pop(0)
            if front in wordDict:
                return True
            prefix = ''
            for c in front:
                prefix += c
                suffix = front[len(prefix):]
                if prefix in wordDict and suffix not in queue:
                    queue.append(suffix)
        return False
