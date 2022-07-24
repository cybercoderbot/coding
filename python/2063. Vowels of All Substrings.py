"""
2063. Vowels of All Substrings
Medium

Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.

 

Example 1:
Input: word = "aba"
Output: 6
Explanation: 
All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
- "b" has 0 vowels in it
- "a", "ab", "ba", and "a" have 1 vowel each
- "aba" has 2 vowels in it
Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6. 

Example 2:
Input: word = "abc"
Output: 3
Explanation: 
All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
- "a", "ab", and "abc" have 1 vowel each
- "b", "bc", and "c" have 0 vowels each
Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.

Example 3:
Input: word = "ltcd"
Output: 0
Explanation: There are no vowels in any substring of "ltcd".

"""


class Solution:
    def countVowels(self, word: str) -> int:
        res = indexSum = 0

        for i, c in enumerate(word, start=1):
            if c in "aeiou":
                indexSum += i
            res += indexSum

        return res


class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        return sum((i+1)*(N-i) for i, x in enumerate(word) if x in "aeiou")
