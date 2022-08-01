"""
438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = Counter(p)
        res = []
        for i, x in enumerate(s):
            freq[x] -= 1
            if len(p) <= i:
                freq[s[i-len(p)]] += 1
            if all(x == 0 for x in freq.values()):
                res.append(i-len(p)+1)
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        M, N = len(p), len(s)
        if M > N:
            return []

        freq, res = defaultdict(int), []
        for c in p:
            freq[c] += 1

        # initial full pass over the window
        for i in range(M-1):
            if s[i] in freq:
                freq[s[i]] -= 1

        # slide the window with stride 1
        for i in range(-1, N-M+1):
            if i > -1 and s[i] in freq:
                freq[s[i]] += 1
            if i+M < N and s[i+M] in freq:
                freq[s[i+M]] -= 1

            # check whether we encountered an anagram
            if all(v == 0 for v in freq.values()):
                res.append(i+1)

        return res
