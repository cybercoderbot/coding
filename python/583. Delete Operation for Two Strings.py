"""
583. Delete Operation for Two Strings
Medium

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 
Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)

        @lru_cache(None)
        def commonSeqLength(i, j):
            """
            Find longest common subsequence length between i~M and j~N
            """
            if i == M or j == N:
                return 0
            if word1[i] == word2[j]:
                return commonSeqLength(i+1, j+1) + 1
            else:
                return max(commonSeqLength(i+1, j), commonSeqLength(i, j+1))

        # subtract the common seq length from both the strings
        # the difference is the number of characters that has to deleted
        return M + N - 2 * commonSeqLength(i=0, j=0)
