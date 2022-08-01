"""
131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()
        res = []
        dfs(s, [], res)

        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(x):
            return x == x[::-1]

        def dfs(path=[], i=1):
            if i == len(s) + 1:
                res.append(list(path))
                return
            for j in range(i, len(s)+1):
                if isPalindrome(s[i-1:j]):
                    path.append(s[i-1:j])
                    dfs(path, j+1)
                    path.pop()
        dfs()

        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Suppose for any given i, we know where all its palindromes end. Say one of them is k, then combining s[i:k+1] and the palindrome partitioning of s[k+1:] should all be included in the answer. To get all palindromes efficiently, we apply similar apprach to that of 5. Longest Palindromic Substring. This would result in an efficient solution.
        """
        p = defaultdict(list)
        for k in range(len(s)):
            for i, j in (k, k), (k, k+1):
                while 0 <= i and j < len(s) and s[i] == s[j]:
                    p[i].append(j)
                    i, j = i-1, j+1

        @lru_cache(None)
        def part(i=0):
            """Return palindrome partitioning of s[i:]"""
            if i == len(s):
                return [[]]
            return [[s[i:j+1]] + y for j in p[i] for y in part(j+1)]

        return part(i=0)
