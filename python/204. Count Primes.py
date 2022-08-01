"""
204. Count Primes
Medium

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
"""


class Solution:
    def countPrimes(self, N: int) -> int:
        """
        Sieve of Eratosthenes
        Iteratively marking multiples of prime factors non-prime
        """
        if N <= 2:
            return 0

        # 0 and 1 are not a prime
        primes = [True] * N
        primes[0] = primes[1] = False

        # only need to check up to sqrt(N)
        for i in range(2, int(sqrt(N))+1):
            # non-prime factors are useless
            if not primes[i]:
                continue
            for k in range(i*i, N, i):
                primes[k] = False
        return sum(primes)
