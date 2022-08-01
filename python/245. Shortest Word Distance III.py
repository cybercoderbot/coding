"""
245. Shortest Word Distance
Easy

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
"""


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        """
        243. Shortest Word Distance
        Scan through words and mark the locations of word1 and word2.
        Time: O(N), Space: O(1)
        """
        res = x = y = inf
        for i, word in enumerate(words):
            if word == word1:
                x = i
            elif word == word2:
                y = i
            res = min(res, abs(x - y))
        return res


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        """
        245. Shortest Word Distance III
        The approach here is quite similar to that of 243, with difference 
        that word1 and word2 could be the same. 
        """
        res = x = y = inf
        for i, word in enumerate(words):
            if word == word1:
                x = i
            if word == word2:
                y = x if word1 == word2 else i
            res = min(res, abs(x - y))
        return res


class WordDistance:
    """
    244. Shortest Word Distance II
    """

    def __init__(self, words: List[str]):
        self.loc = defaultdict(list)
        for i, w in enumerate(words):
            self.loc[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = inf
        loc1, loc2 = self.loc[word1], self.loc[word2]
        i1 = i2 = 0
        while i1 < len(loc1) and i2 < len(loc2):
            res = min(res, abs(loc1[i1] - loc2[i2]))
            if loc1[i1] < loc2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res
