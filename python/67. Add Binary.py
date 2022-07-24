"""
67. Add Binary
Easy

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a, b = list(a), list(b)
        carry = 0
        res = ''

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            res += str(carry % 2)
            carry //= 2

        return res[::-1]
