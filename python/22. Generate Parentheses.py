"""
22. Generate Parentheses
Medium

Given N pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, N: int) -> List[str]:

        def backtrack(candidate, opening, closing):
            """
            Populate res while backtracking
            opening: number of "(" already tried
            closing: number of ")" already tried
            """
            if len(candidate) == 2 * N:
                res.append("".join(candidate))

            if opening < N:
                candidate.append("(")
                backtrack(candidate, opening+1, closing)
                candidate.pop()

            if closing < opening:
                candidate.append(")")
                backtrack(candidate, opening, closing+1)
                candidate.pop()

            return

        res = []
        backtrack(candidate=[], opening=0, closing=0)

        return res
