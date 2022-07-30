"""
633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Solution 1: Sqrt

        Since a ^ 2 + b ^ 2 = c = > a = sqrt(c - b ^ 2) = > a <= sqrt(c).
        Traverse a in range[0..sqrt(c)], check if there exists bSquare(where bSquare=c - a ^ 2) and bSquare is a square number then return True.
        """
        MAX = int(sqrt(c))+1

        for a in range(MAX):
            b = sqrt(c - a*a)
            if b == int(b):
                return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Solution 2: Two Pointers 
        We can search a pair of (left, right), so that left^2 + right^2 = c.
        Start with left = 0, right = int(sqrt(c)).
        while left <= right:
            Let sm = left^2 + right^2.
            If sm == c then we found a perfect match -> return True
            Else if sm < c, we need to increase sm, so left += 1.
            Else we need to decrease sm, so right -= 1.
        """

        left = 0
        right = int(sqrt(c))

        while left <= right:
            sm = left * left + right * right
            if sm == c:
                return True
            if sm < c:
                left += 1
            else:
                right -= 1
        return False
