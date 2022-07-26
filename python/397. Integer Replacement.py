"""
397. Integer Replacement
Medium

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

 
Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2
"""


class Solution:

    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        """
        DP, recursion
        """
        if n == 1:
            return 0
        if not n & 1:
            return self.integerReplacement(n//2) + 1

        x = self.integerReplacement(n+1)
        y = self.integerReplacement(n-1)

        return min(x, y) + 1


class Solution:
    def integerReplacement(self, n: int) -> int:
        """Return num of steps to reach 1 via BFS."""

        queue = [n]
        seen = set()
        res = 0

        while queue:
            tmp = []
            for n in queue:
                if n in seen:
                    continue
                seen.add(n)
                if n == 1:
                    return res
                if n & 1 == 0:
                    tmp.append(n//2)
                else:
                    tmp.extend([n-1, n+1])
            res += 1
            queue = tmp
