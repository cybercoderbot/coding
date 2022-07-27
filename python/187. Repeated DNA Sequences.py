"""
187. Repeated DNA Sequences
Medium

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        freq = defaultdict(int)
        for i in range(len(s)-9):
            seq = s[i:i+10]
            freq[seq] += 1

        return [k for k, v in freq.items() if v > 1]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, seen = set(), set()
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in seen:
                res.add(seq)
            seen.add(seq)
        return res
