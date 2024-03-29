"""
389. Find the Difference
Easy

You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.



Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"
"""


class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        """
        via sum(O(N) time & O(1) space)
        """
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        via xor(O(N) time & O(1) space)
        """
        return chr(reduce(xor, map(ord, s+t)))


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        via sort(O(NlogN) time & O(N) space(could be reduced to O(1)))
        """
        return next(tt for ss, tt in zip_longest(sorted(s), sorted(t)) if ss != tt)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        via Counter(O(N) time & O(N) space)
        """
        return list((Counter(t) - Counter(s)).keys()).pop()


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        via Counter(O(N) time & O(N) space)
        """
        freq = {}
        for x in s:
            freq[x] = freq.get(x, 0) + 1

        for y in t:
            if not freq.get(y, 0):
                return y
            freq[y] -= 1
        return
