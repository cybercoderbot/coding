"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(int)

        for c in s:
            m[c] += 1

        for c in t:
            m[c] -= 1

        return all(x == 0 for x in m.values())


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for c in s:
            dict1[c] += 1

        for c in t:
            dict2[c] += 1

        return dict1 == dict2
