"""
791. Custom Sort String
Medium

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.


Example 2:
Input: order = "cbafg", s = "abcd"
Output: "cbad"

"""


# Solution
# This is in fact an easy custom sorting application. Here, the relative order of characters are defined by their
# positions in S. For those characters who don't appear in S, their order is not defined. As a result,
# one could use any value for them. Here, I've chosen 26, but it is really okay to use any value for them.

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda x: hmap.get(x, 26)))
