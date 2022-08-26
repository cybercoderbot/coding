"""
16. 3Sum Closest
Medium

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        3Sum -> sort array
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        N = len(nums)

        for i in range(N-2):
            j, k = i+1, N-1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == target:
                    return sum3

                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                if sum3 < target:
                    j += 1
                elif sum3 > target:
                    k -= 1

        return res
