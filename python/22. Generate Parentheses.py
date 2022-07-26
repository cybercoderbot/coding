"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, N: int) -> List[str]:

        def backtrack(candidate, left, right):
            if len(candidate) == 2 * N:
                res.append("".join(candidate))
                return

            if left < N:
                candidate.append("(")
                backtrack(candidate, left+1, right)
                candidate.pop()

            if right < left:
                candidate.append(")")
                backtrack(candidate, left, right+1)
                candidate.pop()

        res = []
        backtrack([], 0, 0)

        return res
