"""
1130. Minimum Cost Tree From Leaf Values
Medium

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

Example 1:
Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

Example 2:
Input: arr = [4,11]
Output: 44
"""


from functools import lru_cache


class Solution:
    def mctFromLeafValues(self, nums: List[int]) -> int:
        """
        Solution1: Greedy algorithm
        Recursively locate the min val and combine it with its smaller neighbor.
        Time: O(N ^ 2)
        Space: O(1)
        """

        res = 0
        while len(nums) > 1:
            i = nums.index(min(nums))
            j = max(0, i-1)
            res += nums.pop(i) * min(nums[j:i+1])
        return res


class Solution:
    def mctFromLeafValues(self, nums: List[int]) -> int:
        """
        Solution 2: Stack soluton
        We decompose a hard problem into a easier one: 503. Next Greater Element II
        Just find the next greater element in the array, on the left and one right.

        Time: O(N) for one pass
        Space: O(N) for stack in the worst cases
        """

        res = 0
        stack = [inf]

        for x in nums:
            while stack[-1] <= x:
                mid = stack.pop()
                res += mid * min(stack[-1], x)
            stack.append(x)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res


class Solution:
    def mctFromLeafValues(self, nums: List[int]) -> int:

        res = 0
        stack = []

        for x in nums:
            while stack and stack[-1] <= x:
                mid = stack.pop()
                if stack:
                    res += mid * min(stack[-1], x)
                else:
                    res += mid * x
            stack.append(x)

        for i in range(1, len(stack)):
            res += stack[i-1] * stack[i]

        return res


class Solution:
    def mctFromLeafValues(self, nums: List[int]) -> int:
		"""
		DP (slower than the above greedy alg)
		"""

        @lru_cache(None)
        def dp(i, j):
            """Return """
            if i+1 == j:
                return 0

            return min(max(nums[i:k]) * max(nums[k:j]) + dp(i, k) + dp(k, j) for k in range(i+1, j))

        return dp(i=0, j=len(nums))
