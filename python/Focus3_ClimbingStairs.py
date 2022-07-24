"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3

Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    @lru_cache(None)
    # Top down, not efficient - TLE
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    # Bottom up, O(n) space
    def climbStairs(self, n):
        if n == 1:
            return 1
        cache = [0] * n
        cache[0], cache[1] = 1, 2
        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[-1]


class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a+b
        return a


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]


"""
1137. N-th Tribonacci Number
Easy

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 
Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
"""


class Solution:
    def tribonacci(self, N: int) -> int:
        if N == 0:
            return 0

        if N < 3:
            return 1

        x, y, z = 0, 1, 1
        for _ in range(N-2):
            x, y, z = y, z, x + y + z
        return z
