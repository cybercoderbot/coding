"""
32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Let dp[i] be the number of longest valid parentheses ended with the i-1 position of s, 
        then dp[i+1] = dp[p] + i - p + 1, where p is the position of '(' matching current ')'
        """
        N = len(s)
        dp = [0]*(N + 1)
        stack = []
        for i in range(N):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i+1] = dp[p] + i - p + 1
        return max(dp)
