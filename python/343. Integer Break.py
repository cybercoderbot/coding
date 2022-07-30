"""
343. Integer Break
Medium

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Bottom up DP
        """

        res = [None, 1] + [0] * (n-1)
        for k in range(2, n+1):
            for i in range(1, k//2+1):
                res[k] = max(res[k], max(i, res[i]) * max(k-i, res[k-i]))
        return res[-1]


class Solution:
    @lru_cache(None)
    def integerBreak(self, n: int) -> int:
        """
        Top-down DP
        Return the max product by splitting n.
        """
        if n == 1:
            return 1
        return max(max(i, self.integerBreak(i)) * max(n-i, self.integerBreak(n-i)) for i in range(1, n//2+1))


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Approach 2 - math

        An simple explanation:
        The first thing we should consider is : What is the max product if we break a number N into two factors?

        I use a function to express this product: f = x * (N-x)

        When x=N/2, we get the maximum of this function.

        However, factors should be integers. Thus the maximum is (N/2)*(N/2) when N is even or (N-1)/2 *(N+1)/2 when N is odd.

        When the maximum of f is larger than N, we should do the break.

        (N/2) * (N/2) >= N, then N>=4

        (N-1)/2 *(N+1)/2 N>=5, then N >= 5

        These two expressions mean that factors should be less than 4, otherwise we can do the break and get a better product. The factors in last result should be 1, 2 or 3. Obviously, 1 should be abandoned. Thus, the factors of the perfect product should be 2 or 3.

        If an optimal product contains a factor f >= 4, then you can replace it with factors 2 and f-2 without losing optimality, as 2*(f-2) = 2f-4 >= f. So you never need a factor greater than or equal to 4, meaning you only need factors 1, 2 and 3 (and 1 is of course wasteful and you'd only use it for n=2 and n=3, where it's needed).

        For the rest, 3*3 is simply better than 2*2*2, so you'd never use 2 more than twice.

        """

        if n == 2:
            return 1
        if n == 3:
            return 2

        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
