"""
227. Basic Calculator II
Medium

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 
Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

"""


class Solution:
    def calculate(self, s):
        """
        Use a stack to record s
        """
        x = 0
        stack = []
        sign = "+"

        for i, c in enumerate(s):
            if c.isdigit():
                x = 10 * x + int(c)

            if c in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(x)
                elif sign == "-":
                    stack.append(-x)
                elif sign == "*":
                    stack.append(stack.pop() * x)
                else:
                    stack.append(int(stack.pop() / x))
                x = 0
                sign = c

        return sum(stack)
