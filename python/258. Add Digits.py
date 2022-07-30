"""
258. Add Digits
Easy

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

"""


class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            x = 0
            while num:
                x += num % 10
                num = num//10
            num = x

        return num
