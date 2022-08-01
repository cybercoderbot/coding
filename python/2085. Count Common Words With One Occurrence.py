"""
2085. Count Common Words With One Occurrence
Easy

Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

Example 1:
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

Example 2:
Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.

Example 3:
Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".
"""


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = Counter(words1)
        dict2 = Counter(words2)
        return sum(dict1[key] == dict2[key] == 1 for key in dict2)


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1, freq2, freq3 = map(Counter, (words1, words2, set(words2)))
        return len(freq1.items() & freq2.items() & freq3.items())