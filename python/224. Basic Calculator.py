"""
224. Basic Calculator
Hard

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


class Solution:
    def calculate(self, s: str) -> int:

        sign, stack = 1, []
        res, x = 0, 0

        for c in s:
            if c.isdigit():
                x = 10*x + int(c)

            elif c in "+-":
                res += sign * x
                x = 0
                sign = [-1, 1][c == "+"]

            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif c == ")":
                res += sign * x
                res *= stack.pop()
                res += stack.pop()
                x = 0

        return res + sign * x


class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return res
