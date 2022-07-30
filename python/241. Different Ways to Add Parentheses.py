"""
241. Different Ways to Add Parentheses
Medium

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""


class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:

        if s.isdigit():
            return [int(s)]

        res = []

        def str2num(x, y, op):
            return eval(str(x) + op + str(y))

        for i in range(len(s)):
            if s[i] in "-+*":
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                res.extend(str2num(x, y, s[i]) for x in left for y in right)

        return res


class Solution:

    def compute(self, left, right, op):
        return [eval(str(x) + op + str(y)) for x in left for y in right]

    def diffWaysToCompute(self, s: str, m={}) -> List[int]:

        if s.isdigit():
            return [int(s)]

        res = []
        for i, c in enumerate(s):
            if c in "+-*":
                left = self.diffWaysToCompute(s[: i])
                right = self.diffWaysToCompute(s[i+1:])
                res.extend(self.compute(left, right, c))

        return res
