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


"""
Define fn(i) to be the sentences formed by s[i:]. Then, the recursion satisfies

fn(i) = [[word] + x for x in fn(i + len(word)] for word in wordDict if s[i:].startswith(word)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)  # edit: better performance

        @lru_cache(None)
        def search(i):
            """Return sentences of s[i:]"""
            if i == len(s):
                return [[]]

            res = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    res.extend([s[i:j]] + x for x in search(j))
            return res

        words = search(i=0)
        return [" ".join(x) for x in words]


"""
The bottom-up implementation is very easy to go TLE. The reason is that it doesn't a lot of unnecessary calculations while top-down only does what's required.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        @lru_cache(None)
        def search(i):
            """Return sentences from s[:i]"""
            if i == 0:
                return [[]]

            res = []
            for word in wordDict:
                start = i-len(word)
                if s[start:i] == word:
                    res.extend([x + [word] for x in search(start)])
            return res

        return [" ".join(x) for x in search(i=len(s))]
