"""
371. Sum of Two Integers
Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
"""


class Solution(object):
    def getSum(self, a: int, b: int) -> int:

        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        while b:
            carry = ((a & b) << 1) % MASK
            a = (a ^ b) % MASK
            b = carry

        if a <= MAX_INT:
            return a
        else:
            return ~((a & MAX_INT) ^ MAX_INT)
