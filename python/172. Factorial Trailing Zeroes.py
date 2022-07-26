"""
172. Factorial Trailing Zeroes
Medium


Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0
"""


"""
This question is pretty straightforward.

Because all trailing 0 is from factors 5 * 2.

But sometimes one number may have several 5 factors, for example, 25 have two 5 factors, 125 have three 5 factors. In the n! operation, factors 2 is always ample. So we just count how many 5 factors in all number from 1 to n.
"""


"""
10 is the product of 2 and 5. In n!, we need to know how many 2 and 5, and the number of zeros is the minimum of the number of 2 and the number of 5.

Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.
"""


class Solution:

    def trailingZeroes(self, n: int) -> int:
        """
        Num of 0's -> num of 2's and num of 5's -> num of 5's
        """
        res = 0
        while n > 0:
            res += n//5
            n //= 5

        return res


class Solution:

    @lru_cache(None)
    def trailingZeroes(self, n: int) -> int:

        if n == 0:
            return 0

        return n // 5 + self.trailingZeroes(n // 5)
