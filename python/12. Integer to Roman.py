"""
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman number.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        12. Integer to Roman
        """
        roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        res = []
        for k, v in roman.items():
            res.append(num//k * v)
            num %= k
        return "".join(res)


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        12. Integer to Roman
        """
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for x in roman.keys():
            div, mod = divmod(num, x)
            res += div * roman[x]
            num = mod
        return res


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        12. Integer to Roman
        """
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for x in roman.keys():
            res += (num//x) * roman[x]
            num %= x
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        13. Roman to Integer
        Intuitive implementation
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                 "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        res = i = 0
        while i < len(s):
            if s[i:i+2] in roman:
                res += roman[s[i:i+2]]
                i += 2
            else:
                res += roman[s[i:i+1]]
                i += 1
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        13. Roman to Integer
        If a lower value is placed before a higher value, we should subtract
        its value instead of adding it.
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
