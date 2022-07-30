"""
500. Keyboard Row
Easy

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""


class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')

        res = []
        for word in words:
            w = set(word.lower())
            if w.issubset(s1) or w.issubset(s2) or w.issubset(s3):
                res.append(word)
        return res
