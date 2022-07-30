class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        """
        70. Climbing Stairs
        Each time you can either climb 1 or 2 steps.
        Return number of ways to reach to top of n steps.
        Top down DP
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    def climbStairs(self, n):
        """
        70. Climbing Stairs
        Bottom up DP
        Space: O(N)
        """

        if n == 1:
            return 1

        cache = [0] * n
        cache[0], cache[1] = 1, 2

        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[-1]


class Solution:
    def fib(self, N: int) -> int:
        """
        509. Fibonacci Number
        1) F(0) = 0, F(1) = 1
        2) F(n) = F(n - 1) + F(n - 2), for n > 1.
        """

        if N <= 1:
            return N

        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]


class Solution:
    def fib(self, N: int) -> int:
        """
        509. Fibonacci Number
        1) F(0) = 0, F(1) = 1
        2) F(n) = F(n - 1) + F(n - 2), for n > 1.
        """

        a, b = 0, 1
        for _ in range(N):
            a, b = b, a+b
        return a


class Solution:
    def tribonacci(self, N: int) -> int:
        """
        1137. N-th Tribonacci Number

        The Tribonacci sequence Tn is defined as follows: 
        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
        Given n, return the value of Tn.
        """

        if N == 0:
            return 0

        if N < 3:
            return 1

        x, y, z = 0, 1, 1
        for _ in range(N-2):
            x, y, z = y, z, x + y + z
        return z
