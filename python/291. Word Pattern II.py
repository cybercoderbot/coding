"""
291. Word Pattern II
Medium

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.


Example 1:
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"

Example 2:
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"

Example 3:
Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
"""


class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        """
        Backtracking via two maps

        Iterate through each substring in s and each character in p simultaneously, 
        and try each possible mapping. 

        Only recurse if either:
        1) The character in p has not been assigned a mapping
        2) The character in p has been assigned a mapping and it's equal to the substring under consideration

        """

        M, N = len(p), len(s)
        if M > N:
            return False

        m1, m2 = {}, {}

        def backtrack(i: int, j: int):
            if i == M:
                return j == N

            for k in range(j + 1, N + 1):
                sub = s[j:k]
                if p[i] not in m1 and sub not in m2:
                    # tentatively assign p[j] to sub, and recurse
                    m1[p[i]] = sub
                    m2[sub] = p[i]

                    if backtrack(i+1, k):
                        return True

                    m1.pop(p[i])
                    m2.pop(sub)

                elif p[i] in m1 and sub == m1[p[i]]:
                    if backtrack(i+1, k):
                        return True

            return False

        return backtrack(i=0, j=0)


class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:

        def backtrack(i, j):
            """Return True if pattern[i:] can be mapping to s[k:]"""
            if i == len(p):
                return j == len(s)
            if j == len(s):
                return i == len(p)

            if p[i] in m:
                x = len(m[p[i]])
                if m[p[i]] != s[j:j+x]:
                    return False
                return backtrack(i+1, j+x)

            for k in range(j+1, len(s)+1):
                sub = s[j:k]
                if sub not in m:
                    m[p[i]] = sub
                    m[sub] = p[i]
                    if backtrack(i+1, k):
                        return True
                    m.pop(p[i])
                    if p[i] != sub:
                        m.pop(sub)

            return False

        m = defaultdict(int)

        return backtrack(i=0, j=0)
