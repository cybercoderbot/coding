"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        N, i, j = len(nums), 0, 0
        left, right = 0, N-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                i, j = mid, mid
                while i-1 >= 0 and nums[i-1] == target:
                    i -= 1
                while j + 1 < N and nums[j+1] == target:
                    j += 1
                break

        return [i, j]
