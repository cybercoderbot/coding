"""
254. Factor Combinations
Medium

Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

Example 1:
Input: n = 1
Output: []

Example 2:
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]

Example 3:
Input: n = 37
Output: []
"""


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        factors = [k for k in range(2, int(sqrt(n))+1) if n % k == 0]

        def backtrack(i, n):
            """Populate res via a stack."""
            if len(stack) > 0 and stack[-1] <= n:
                res.append(stack + [n])
            for j in range(i, len(factors)):
                if n % factors[j] == 0:
                    stack.append(factors[j])
                    backtrack(j, n//factors[j])
                    stack.pop()

        res, stack = [], []
        backtrack(0, n)
        return res


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        stack = [(n, 2, [])]
        res = []
        while stack:
            n, i, tmp = stack.pop()
            while i * i <= n:
                if n % i == 0:
                    res.append(tmp + [i, n/i])
                    stack.append((n/i, i, tmp+[i]))
                i += 1
        return res


class Solution:
    @lru_cache(None)
    def getFactors(self, n: int) -> List[List[int]]:

        if N <= 1:
            return []

        res = []
        i = 2
        while i * i <= N:
            if N % i:
                i += 1
                continue
            k = N // i
            res.append([i, k])
            subres = self.getFactors(k)
            for r in subres:
                if r[0] >= i:
                    res.append([i] + r)
            i += 1

        return res
