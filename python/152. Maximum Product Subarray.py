"""
152. Maximum Product Subarray
Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


"""
Maximum Product Subarray https://leetcode.com/problems/maximum-product-subarray/?tab=Description

https://www.quora.com/How-do-I-solve-maximum-product-subarray-problems
Use an example: [2,-3,4,-8,0]

Insights:
What if the array has just positive numbers including zero?
A solution of this will maintain max_prod[i] where max_prod[i] is the maximum subarray product ending at i. Then max_prod[i+1] = max(max_prod[i] * nums[i+1], nums[i+1]).
Now how do we change the solution when we allow negative numbers?
Imagine that we have both max_prod[i] and min_prod[i] i.e. max prod ending at i and min prod ending at i. Now if we have a negative number at nums[i+1] and if min_prod[i] is negative, then the product of the two will be positive and can potentially be largest product. Key point is to maintain both max_prod and min_prod such that at iteration i, they refer to the max and min prod ending at index i -1.
You have three choices to make at any position in array.

You can get maximum product by multiplying the current element with
maximum product calculated so far. (might work when current
element is positive).
You can get maximum product by multiplying the current element with
minimum product calculated so far. (might work when current
element is negative).
Current element might be a starting position for maximum product sub
array
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = mn = res = nums[0]
        for n in nums[1:]:
            x = max(n, mx * n, mn * n)
            y = min(n, mx * n, mn * n)
            mx, mn = x, y
            res = max(mx, res)
        return res


class Solution(object):
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


class Solution(object):
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 解题思路：Dynamic programming

        # 用数组positive_max[i]维护原始数组前i个数的子数组乘积中正数的最大值
        # 用数组negative_min[i]维护原始数组前i个数的子数组乘积中负数的最小值

        # 状态转移方程为：

        # if A[x] > 0:
        #   positive_max[x] = max(positive_max[x-1] * A[x], A[x])
        #   negative_min[x] = negative_min[x-1] * A[x]

        # elif A[x] < 0:
        #   positive_max[x] = negative_min[x-1] * A[x]
        #   negative_min[x] = min(positive_max[x-1] * A[x], A[x])

        ans = max(A)
        size = len(A)
        positive_max = [0 for x in range(size)]
        negative_min = [0 for x in range(size)]

        if A[0] > 0:
            positive_max[0] = A[0]
        elif A[0] < 0:
            negative_min[0] = A[0]

        for x in range(1, size):
            if A[x] > 0:
                positive_max[x] = max(positive_max[x-1] * A[x], A[x])
                negative_min[x] = negative_min[x-1] * A[x]

            elif A[x] < 0:
                positive_max[x] = negative_min[x-1] * A[x]
                negative_min[x] = min(positive_max[x-1] * A[x], A[x])

            ans = max(ans, positive_max[x])

        return ans
