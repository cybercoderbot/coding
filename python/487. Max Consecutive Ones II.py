"""
487. Max Consecutive Ones II
Medium

Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Define a slideing window from i to j in which at most one 0 can exist.
        """
        res = count = i = 0
        for j, x in enumerate(nums):
            count += 1 - nums[j]
            while count > 1:
                count -= 1 - nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cur = 0
        pre = -1

        for x in nums:
            if x == 0:
                pre, cur = cur, 0
            else:
                cur += 1
            res = max(res, pre + 1 + cur)
        return res
