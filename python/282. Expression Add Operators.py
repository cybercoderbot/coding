"""
282. Expression Add Operators
Hard

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
"""


class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:

        def backtrack(i, expr, cursum, last):
            if i == N and cursum == target:
                res.append(expr)
                return

            for j in range(i, N):
                if j > i and s[i] == '0':
                    break  # Skip leading zero number
                num = int(s[i:j+1])
                if i == 0:
                    # First num, pick it without adding any operator
                    backtrack(j+1, str(num), num, num)
                else:
                    backtrack(j+1, expr + "+" + str(num), cursum + num, num)
                    backtrack(j+1, expr + "-" + str(num), cursum - num, -num)
                    # Can imagine with example: 1+2*3*4
                    backtrack(j+1, expr + "*" + str(num), cursum -
                              last + last * num, last * num)

        res = []
        N = len(s)
        backtrack(0, "", 0, 0)
        return res
