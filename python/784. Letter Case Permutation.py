"""
784. Letter Case Permutation
Medium


Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
 

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""


# At every position in the string:

# check whether the character is a numeric or an alphabet
# if alpha: convert the character at this position in the string to uppercase and lowercase and recursion at the next in these two new string
# if numeric: skip the character at this position and recursion at the next position of the same string
# append the words to the result list when reached at the end of the list


# Exhaust all possibilities.


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Iterative implementation
        """
        res = [""]
        for c in s:
            res = [x + c1 for x in res for c1 in {c, c.swapcase()}]
        return res


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Recursive implementation 
        """

        def backtrack(i):
            """Populate res via a stack."""
            if i == len(s):
                return res.append("".join(stack))

            for c in {s[i], s[i].swapcase()}:
                stack.append(c)
                backtrack(i+1)
                stack.pop()

        res, stack = [], []
        backtrack(0)
        return res


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        bottom-up
        """

        def fn(i):
            """Return letter case permutation of S[i:]."""
            if i == len(s):
                return [""]
            return [c + x for c in {s[i], s[i].swapcase()} for x in fn(i+1)]

        return fn(0)


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def backtrack(word, i):
            if i == len(word):
                res.append(word)
                return
            if word[i].isalpha():
                w1 = word[:i] + word[i].lower() + word[i+1:]
                backtrack(w1, i+1)
                w2 = word[:i] + word[i].upper() + word[i+1:]
                backtrack(w2, i+1)
            else:
                backtrack(word, i+1)
            return

        res = []
        backtrack(s, 0)

        return res
