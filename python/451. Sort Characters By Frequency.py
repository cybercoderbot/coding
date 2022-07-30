"""
451. Sort Characters By Frequency
Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sort
        Get a frequency table, and sort s based on its frequency. 
        Ties are handled by the relative order of characters.
        """
        freq = Counter(s)
        return "".join(sorted(s, key=lambda x: (-freq.get(x), x)))


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sort frequency table & reconstruct string
        Get a frequency table, sort the frequency table in decreasing order, 
        and reconstruct the string.
        """
        return "".join(c * x for c, x in Counter(s).most_common())


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Bucket sort approach
        """
        freq = Counter(s)
        bucket = [[] for _ in range(len(s)+1)]
        for k, v in freq.items():
            bucket[v].append(k)
        ans = []
        for i in reversed(range(1+len(s))):
            for x in bucket[i]:
                ans.append(i * x)
        return "".join(ans)
