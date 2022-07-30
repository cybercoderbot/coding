"""
243. Shortest Word Distance
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
        Scan through words and mark the locations of word1 and word2.
        Time: O(N), Space: O(1)
        """
        res = i1 = i2 = inf
        for i, word in enumerate(words):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            res = min(res, abs(i1 - i2))
        return res


class WordDistance:
        """
        For a given word, collect its indices in an array.
        For given two words, find their closest indices.

        Time: O(N), Space: O(N)
        """

    def __init__(self, words: List[str]):
 
        self.loc = defaultdict(int)
        for i, word in enumerate(words):
            self.loc[word].append(i)
        return

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
