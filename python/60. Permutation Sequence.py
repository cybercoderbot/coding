"""
60. Permutation Sequence
Hard

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.


Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 123456789
        s = [str(i) for i in range(1, n+1)]

        def backtrack(i):
            if i == n:
                cand = "".join(s)
                res.append(cand)
                return

            for j in range(i, n):
                s[i], s[j] = s[j], s[i]
                backtrack(i+1)
                s[j], s[i] = s[i], s[j]

            return

        cand, res = [], []
        backtrack(i=0)

        res.sort()

        return res[k-1]


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Approach 1: brute force O(N!)
        """
        perms = permutations(range(1, n+1))

        for i, x in enumerate(perms, 1):
            if i == k:
                return "".join(map(str, x))
        return ""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Approach 2:  O(N ^ 2)
        """
        k -= 1
        res = []
        nums = list(range(1, n+1))

        for i in range(n, 0, -1):
            d, k = divmod(k, factorial(i-1))
            res.append(nums.pop(d))

        return "".join(map(str, res))
