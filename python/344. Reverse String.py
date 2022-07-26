"""
344. Reverse String
Easy

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverse(s, i, j):
    if i < j:
        s[i], s[j] = s[j], s[i]
        reverse(s, i+1, j-1)


class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse(s, 0, len(s)-1)
