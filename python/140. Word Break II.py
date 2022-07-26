"""
140. Word Break II
Hard

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # 解题思路: 记忆化搜索
        # 在搜索过程中，使用字典ansDict将已经搜索过的子句的拆解方案记录下来，从而实现DFS的剪枝。

        ansDict = {}

        def dfs(s):
            ans = []
            if s in wordDict:
                ans.append(s)

            for i in range(len(s) - 1):
                prefix, suffix = s[:i+1], s[i+1:]
                if prefix not in wordDict:
                    continue
                # rest = []
                if suffix in ansDict:
                    rest = ansDict[suffix]
                else:
                    rest = dfs(suffix)
                for n in rest:
                    ans.append(prefix + ' ' + n)
            ansDict[s] = ans
            return ans

        return dfs(s)
