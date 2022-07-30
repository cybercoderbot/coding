"""
2089. Find Target Indices After Sorting Array
Easy

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

"""


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, x in enumerate(nums) if x == target]


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Sort: O(NlogN)
        """

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res


class Solution:
    def targetIndices(self, nums, target):
        """
        Find the number of smaller numbers than the target

        Time complexity: O(n)
        Space complexity: O(1)
        """

        start = sum(x < target for x in nums)
        count = sum(x == target for x in nums)
        return range(start, start+count)


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Find the number of smaller numbers than the target

        Time complexity: O(n)
        Space complexity: O(1)
        """

        start = count = 0

        for x in nums:
            if x < target:
                start += 1

            if x == target:
                count += 1

        return range(start, start+count)


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Find the leftmost and rightmost num that's equal to target
        """

        left, right = 0, len(nums)-1
        mid = 0

        while mid <= right:
            if nums[mid] == target:
                mid += 1
            elif nums[mid] < target:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

        return range(left, right+1)
