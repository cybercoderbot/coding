"""
231. Power of Two
Easy

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """iterative implementation"""
        if n <= 0:
            return False
        while n:
            n, r = divmod(n, 2)
            if n and r:
                return False
        return True


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """recursive implementation"""
        if n <= 0:
            return False
        if n % 2:
            return n == 1
        return self.isPowerOfTwo(n//2)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """recursive implementation"""
        if n <= 0:
            return False
        if n % 3:
            return n == 1
        return self.isPowerOfThree(n//3)


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """recursive implementation"""
        if n <= 0:
            return False
        if n % 4:
            return n == 1
        return self.isPowerOfFour(n//4)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        return n > 0 and 2**int(log2(n)) == n


"""
When it comes to power of 2, special methods can be used. It is not difficult to find that power of two only has 1 set bit. Utilizing this property, we could propose the below much easier 1-liners.

Essentially what's implemented here reflects Kernighan's algo. 
Given a number, n & (n-1) unset the last set bit. Here, we require n has exactly one set bit.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n == n & (-n)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 2**31 % n == 0
