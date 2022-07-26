"""
267. Palindrome Permutation II
Medium

Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.


Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
"""


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        freq = Counter(s)

        nodd = sum(x & 1 for x in freq.values())
        if nodd > 1:
            return []

        res = []
        vals, mid = [], ""
        for k, v in freq.items():
            vals.extend([k] * (v//2))
            if v & 1:
                mid = k

        def backtrack(i):
            """Permutation without duplicates."""
            if i == len(vals):
                res.append("".join(vals) + mid + "".join(vals[::-1]))
                return

            seen = set()
            for j in range(i, len(vals)):
                if vals[j] in seen:
                    continue

                seen.add(vals[j])
                vals[i], vals[j] = vals[j], vals[i]
                backtrack(i+1)
                vals[i], vals[j] = vals[j], vals[i]

            return

        backtrack(0)

        return res
