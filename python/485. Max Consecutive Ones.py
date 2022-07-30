"""
485. Max Consecutive Ones
Easy

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Scan through nums and keep track of current length of consecutive ones. 
        If the current count is larger than the res, update the res.
        """
        res = count = 0
        for x in nums:
            if x:
                count += 1
            else:
                count = 0
            res = max(res, count)
        return res
