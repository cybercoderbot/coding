"""
273. Integer to English Words
Hard

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Here, separate the number in English into two parts

        1)thousands, millions, billions
        2)hundreds-tens-digits
        Within each 1000 unit, the code to create hundreds-tens-digits can be done through a helper function.
        """

        words = {1: "One",   11: "Eleven",    10: "Ten",
                 2: "Two",   12: "Twelve",    20: "Twenty",
                 3: "Three", 13: "Thirteen",  30: "Thirty",
                 4: "Four",  14: "Fourteen",  40: "Forty",
                 5: "Five",  15: "Fifteen",   50: "Fifty",
                 6: "Six",   16: "Sixteen",   60: "Sixty",
                 7: "Seven", 17: "Seventeen", 70: "Seventy",
                 8: "Eight", 18: "Eighteen",  80: "Eighty",
                 9: "Nine",  19: "Nineteen",  90: "Ninety"}

        units = {9: "Billion", 6: "Million", 3: "Thousand", 0: ""}

        def num2word(n):
            """Return English words of n (0-999) in array."""
            if not n:
                return []
            elif n < 20:
                return [words[n]]
            elif n < 100:
                return [words[n-n % 10]] + num2word(n % 10)
            else:
                return [words[n//100], "Hundred"] + num2word(n % 100)

        res = []

        for i, u in units.items():
            n, num = divmod(num, 10**i)
            res.extend(num2word(n))
            if n and u:
                res.append(u)
        return " ".join(res) or "Zero"
