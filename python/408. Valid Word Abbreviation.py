"""
408. Valid Word Abbreviation
Easy

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".


Solution:

The idea is to compare word and abbr char by char. If abbr[j] is char, check if word[i] == abbr[j]; If yes, continue to the next char; if no, return False.

If abbr[j] is a digit, then scan abbr and get the number N; then add N to i to skip scanning N chars in word. Corner case here is to check if N starts with 0.

At the end, check if i and j have both reached the end of word and abbr.

"""


class Solution:
    def validWordAbbreviation(self, word, abbr):
        i, j = 0, 0
        N1, N2 = len(word), len(abbr)

        while i < N1 and j < N2:
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == "0":
                    return False
                tmp = ""
                while j < N2 and abbr[j].isdigit():
                    tmp += abbr[j]
                    j += 1
                i += int(tmp)

        return i == len(word) and j == len(abbr)
