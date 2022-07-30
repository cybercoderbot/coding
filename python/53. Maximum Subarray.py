"""
53. Maximum Subarray
Medium

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's algorithm (search Maximum_subarray_problem)

        For an array s whose ith element represents the largest contiguous sum 
        ending at nums[i]. Then,

        s[i+1] = max(s[i], 0) + nums[i]

        Bottom-up DP
        Time: O(N), Space: O(1)
        """

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, val = -inf, 0

        for x in nums:
            val = max(0, val) + x
            res = max(res, val)
        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = val = 0
        for x in nums:
            val = max(0, val + x)
            res = max(res, val)
        return res
