"""
409. Longest Palindrome
Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired = set()

        for c in s:
            if c in unpaired:
                pairs += 1
                unpaired.remove(c)
            else:
                unpaired.add(c)

        if unpaired:
            return pairs * 2 + 1
        else:
            return pairs * 2
