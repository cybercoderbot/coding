"""
916. Word Subsets
Medium

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
"""


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        The idea here is to use counters: we need to find elements from words1, for which each string from words2 have less or equal frequencies for each symbol. Let us create freq counter, with maximal values for each letter, that is if we have words2 = [abb, bcc], then we have freq = {a:1, b:2 ,c:2}. In python it can be written using | symbol.

        Second step is for each string a from words1 calcuate counter and check that it is bigger for each element than freq. Again in python it can be done in very short way, using not freq - Counter(W).

        For each word in words2,
        we use function counter to count occurrence of each letter.
        We take the maximum occurrences of counts, and use it as a filter of words1.

        Time: is O(M + N)
        Space: is O(M)

        """

        freq = collections.Counter()
        for w in words2:
            # |= : dict union
            freq |= collections.Counter(w)

        return [w for w in words1 if not freq - Counter(w)]
