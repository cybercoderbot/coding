"""
856. Score of Parentheses
Medium

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Approach 0: Stack
        res record the score at the current layer level.

        If we meet '(',
        we push the current score to stack,
        enter the next inner layer level,
        and reset res = 0.

        If we meet ')',
        the res score will be doubled and will be at least 1.
        We exit the current layer level,
        and set res += stack.pop() + res

        Complexity: O(N) time and O(N) space
        """

        stack, res = [], 0
        for c in s:
            if c == '(':
                stack.append(res)
                res = 0
            else:
                # "()" -> score 1
                new = stack.pop() + max(res, 1)
                res += new
        return res


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Approach 1: Array
        Same as stack, I do it with an array.
        We change a pointer instead of pushing/popping repeatedly.

        Complexity: O(N) time and O(N) space
        """

        res, i = [0] * 30, 0
        for c in s:
            i += 1 if c == '(' else -1
            res[i] = res[i] + max(res[i + 1] * 2, 1) if c == ')' else 0
        return res[0]


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Approach 2: O(1) Space
        We count the number of layers.
        If we meet '(' layers number l++
        else we meet ')' layers number l--

        If we meet "()", we know the number of layer outside,
        so we can calculate the score res += 1 << l.
        """
        res = temp = 0
        for a, b in zip(s[:-1], s[1:]):
            if a + b == '()':
                res += 2 ** temp

            if a == '(':
                temp += 1
            else:
                temp -= 1

        return res
