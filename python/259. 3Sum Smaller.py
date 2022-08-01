"""
259. 3Sum Smaller
Medium

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
"""


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Sort nums in ascending order. Scan through nums with a pointer i. 
        At any place, define two pointers initialized at i+1 and N-1.
        Time: O(N), Space: O(1)
        """
        nums.sort()
        res, N = 0, len(nums)
        for i in range(N):
            left, right = i+1, N-1
            while left < right:
                if nums[i] + nums[left] + nums[right] >= target:
                    right -= 1
                else:
                    res += right - left
                    left += 1
        return res
