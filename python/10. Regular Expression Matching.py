"""
10. Regular Expression Matching
Hard

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".       



Solution
This problem can be solved using dynamic programming. Define dfs(i, j) to represent if s[i:] and p[j:] matches.

1. if j == len(p), return True if i == len(s); otherwise, return False;
2. if p[j+1] == "*", check if s[i:] matches p[j+2:] (zero occurrence) or s[i] matches p[j] and s[i+1:] matches p[j:] (one or more occurrences);
3. if p[j+1] != "*", check if s[i] == p[j] and s[i:] matches p[j:].

"""

def dfs(s, p, i, j): 
    """Return True if s[i:] matches p[j:]"""
    M, N = len(s), len(p)

    if j == N: 
        return i == M

    match = i < M and p[j] in (s[i], ".")
    # match = i < M and (s[i] == p[j] or p[j] == ".")

    if j+1 < N and p[j+1] == "*": 
        return dfs(s, p, i, j+2) or (match and dfs(s, p, i+1, j))
    else: 
        return match and dfs(s, p, i+1, j+1)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """dynamic programming"""
        return dfs(s, p, 0, 0)
        