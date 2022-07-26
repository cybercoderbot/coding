"""
72. Edit Distance
Hard

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:

    @lru_cache(None)
    def minDistance(self, word1, word2):
        """Naive recursive solution"""

        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        insert = self.minDistance(word1, word2[1:]) + 1
        delete = self.minDistance(word1[1:], word2) + 1
        replace = self.minDistance(word1[1:], word2[1:]) + 1

        return min(insert, replace, delete)


class Solution:

    def minDistance(self, word1, word2, cache={}):
        """Memoized solution"""

        if not word1 and not word2:
            return 0

        if not len(word1) or not len(word2):
            return len(word1) or len(word2)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        if (word1, word2) not in cache:
            inserted = self.minDistance(word1, word2[1:]) + 1
            deleted = self.minDistance(word1[1:], word2) + 1
            replaced = self.minDistance(word1[1:], word2[1:]) + 1
            cache[(word1, word2)] = min(inserted, deleted, replaced)

        return cache[(word1, word2)]


class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
