"""
2036. Maximum Alternating Subarray Sum
Medium

A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within an array.

The alternating subarray sum of a subarray that ranges from index i to j (inclusive, 0 <= i <= j < nums.length) is nums[i] - nums[i+1] + nums[i+2] - ... +/- nums[j].

Given a 0-indexed integer array nums, return the maximum alternating subarray sum of any subarray of nums.


Example 1:

Input: nums = [3,-1,1,2]
Output: 5
Explanation:
The subarray [3,-1,1] has the largest alternating subarray sum.
The alternating subarray sum is 3 - (-1) + 1 = 5.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 2
Explanation:
The subarrays [2], [2,2,2], and [2,2,2,2,2] have the largest alternating subarray sum.
The alternating subarray sum of [2] is 2.
The alternating subarray sum of [2,2,2] is 2 - 2 + 2 = 2.
The alternating subarray sum of [2,2,2,2,2] is 2 - 2 + 2 - 2 + 2 = 2.
Example 3:

Input: nums = [1]
Output: 1
Explanation:
There is only one non-empty subarray, which is [1].
The alternating subarray sum is 1.

"""

"""
Solution
At each index we have 3 options to append the new number num = nums[i] to the subarray:

Add num to the subarray that ends with - . In that case we add. Math.max(lastMinus + num, ...)
Add num to the subarray that ends with+. Int that case we substract it. lastPlus - num
Start a new subarray. Because every subarray starts with +, the only way is to just take the num. Math.max(..., num)"""


class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:

        res = lastMinus = lastPlus = -inf

        for x in nums:
            temp = lastPlus
            lastPlus = max(lastMinus + x, x)
            lastMinus = temp - x
            res = max(res, lastMinus, lastPlus)

        return res
