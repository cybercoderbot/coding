"""
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: [2,2,2,2,2]
Output: 2
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        O(N) time, O(N) space
        """
        N = len(nums) - 1
        seen = [0] * (N+1)
        for x in nums:
           if seen[x]:
                return x
            seen[x] = 1
        return -1 


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        O(N) time, O(1) space
        """
        for x in nums:
            if nums[abs(x)] < 0:
                res = abs(x)
                break
            nums[abs(x)] = -nums[abs(x)]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return res

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        O(N) time, O(1) space
        """
        slow = nums[nums[0]]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
