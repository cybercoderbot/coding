"""
290. Word Pattern
Easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(p):
            return False
        return len(set(s)) == len(set(p)) == len(set(zip(s, p)))


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s, p = s.split(), list(p)
        return list(map(s.index, s)) == list(map(p.index, p))


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        m1 = {}
        m2 = {}

        s = s.split(' ')
        if len(s) != len(p):
            return False

        for c, w in zip(p, s):
            if c not in m1:
                if w in m2:
                    return False
                else:
                    m1[c] = w
                    m2[w] = c
            else:
                if m1[c] != w:
                    return False
        return True
