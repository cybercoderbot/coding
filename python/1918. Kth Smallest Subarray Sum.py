"""
1918. Kth Smallest Subarray Sum
Medium

Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.
A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.

Example 1:
Input: nums = [2,1,3], k = 4
Output: 3
Explanation: The subarrays of [2,1,3] are:
- [2] with sum 2
- [1] with sum 1
- [3] with sum 3
- [2,1] with sum 3
- [1,3] with sum 4
- [2,1,3] with sum 6 
Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.
"""


class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:

        def nsubs(target):
            """Return number of subarrays sums <= target """
            res = total = left = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > target:  # sliding window
                    total -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        low, high = 0, sum(nums)
        while low < high:
            mid = (low + high) // 2
            if nsubs(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
