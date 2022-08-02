"""
1047. Remove All Adjacent Duplicates In String
Easy

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Keep a stack as a characters stack.
        Iterate characters of s one by one.
        1) If the next character is same as the last character in stack,
        pop the last character from stack.
        In this way, we remove a pair of adjacent duplicates characters.
        2) If the next character is different, we append it to the end of stack.
        """
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        If duplicate refers to more than 2 adjacent letters, 
        a duplicate flag would be needed.
        """
        stack = []
        dup = None
        for c in s:
            if dup:
                if dup == c:
                    continue
                else:
                    dup = None
            if stack and stack[-1] == c:
                dup = stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


"""
1209. Remove All Adjacent Duplicates in String II
Medium

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""


class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Once you have identified that stack solves this problem, the logic is quite straightforward. We just need to track consecutive occurences of a character. 
        If count matches k, we pop the element from stack.
        """

        # stack: (c, count)
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        return ''.join(c * x for c, x in stack)
