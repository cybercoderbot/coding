"""
1087. Brace Expansion
Medium

You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.

Example 1:
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

Example 2:
Input: s = "abcd"
Output: ["abcd"]

Constraints:
1 <= s.length <= 50
s consists of curly brackets '{}', commas ',', and lowercase English letters.
s is guaranteed to be a valid input.
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
"""


class Solution:
    def expand(self, s: str) -> List[str]:
        res = [""]
        i = 0
        while i < len(s):
            if s[i] == "{":
                j = i+1
                while s[j] != "}":
                    j += 1
                options = s[i+1:j].split(",")
                res = [r + x for r in res for x in options]
                i = j + 1
            else:
                res = [r + s[i] for r in res]
                i += 1

        return sorted(res)


class Solution:
    def expand(self, s: str) -> List[str]:
        N = len(s)
        res = []

        def dfs(cand, i):
            if i == N:
                res.append(cand)
                return
            if s[i] == "{":
                j = i+1
                while s[j] != "}":
                    j += 1
                options = s[i+1: j].split(",")
                for c in options:
                    dfs(cand + c, j + 1)
            else:
                dfs(cand + s[i], i + 1)

        dfs("", 0)
        return sorted(res)
