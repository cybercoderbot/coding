"""
1160. Find Words That Can Be Formed by Characters
Easy

You are given an array of strings words and a string chars. 
A string is good if it can be formed by characters from chars (each can only be used once). 
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        res = 0
        for word in words:
            if Counter(word) <= freq:
                res += len(word)
        return res


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """ Time: O(N), Space: O(N) """
        freq = collections.Counter(chars)
        return sum(len(w) for w in words if collections.Counter(w) <= freq)


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        fc = {}
        for c in chars:
            fc[c] = 1 + fc.get(c, 0)

        res = 0
        for word in words:
            fw = {}
            for c in word:
                fw[c] = 1 + fw.get(c, 0)
            if all(fw[c] <= fc.get(c, 0) for c in fw):
                res += len(word)
        return res
