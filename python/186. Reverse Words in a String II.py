"""
186. Reverse Words in a String II
Medium

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]
"""


class Solution:

    @staticmethod
    def reverse(s, i, j):
        """Reverse s[lo:hi+1]."""
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1

        return

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        N = len(s)
        self.reverse(s, 0, N-1)

        left = 0
        for i, c in enumerate(s):
            if c == " ":
                self.reverse(s, left, i - 1)
                left = i + 1
        self.reverse(s, left, N-1)


class Solution:

    @staticmethod
    def reverse(s, i, j):
        """Reverse s[i:j+1]."""
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1

        return

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Reverse s. Then, reverse each word.
        Time complexity O(N)
        Space complexity O(1)
        """

        N = len(s)
        self.reverse(s, 0, N-1)

        low = 0
        for i in range(N+1):
            if i == N or s[i] == " ":
                self.reverse(s, low, i-1)
                low = i + 1

        return
