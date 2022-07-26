''' 633. Sum of Square Numbers
DescriptionHintsSubmissionsDiscussSolution

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False
'''


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**.5)**2 == N

        return any(is_square(c - x*x) for x in range(int(c**.5) + 1))
