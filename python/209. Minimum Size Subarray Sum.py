"""
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""


"""
Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding window with 2 pointers
        The result is initialized as res = N + 1.
        One pass, remove the value from sum s by doing target -= nums[right].
        If target <= 0, it means nums[i] + ... + nums[j] >= sum that we want.
        Then we update the res = min(res, right - left + 1)
        Finally we return the result res.
        Time O(N), Space O(1)
        """

        left, N = 0, len(nums)
        res = N + 1

        for right in range(N):
            target -= nums[right]
            while target <= 0:
                res = min(res, right-left + 1)
                target += nums[left]
                left += 1
        return res % (N + 1)
