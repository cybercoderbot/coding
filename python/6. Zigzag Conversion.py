"""
6. Zigzag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a 
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int N)
 
Example 1:
Input: s = "PAYPALISHIRING", N = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", N = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", N = 1
Output: "A"
"""


class Solution:
    def convert(self, s: str, N: int) -> str:
        """
        P   A   H   N
        A P L S I I G
        Y   I   R
        """
        if N == 1:
            return s

        rows = [""] * N
        i, down = 0, 1

        for c in s:
            rows[i] += c
            i += down
            if i in (0, N-1):
                down *= -1

        # s = "PAYPALISHIRING"
        # rows = ["PAHN", "APLSIIG", "YIR"]
        # "PAHNAPLSIIGYIR"
        return "".join(rows)
