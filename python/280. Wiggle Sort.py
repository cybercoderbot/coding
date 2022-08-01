"""
280. Wiggle Sort
Medium

Given an integer array nums, reorder it such that 
nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

Example 1:
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.

Example 2:
Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]
"""

"""
The rule is:

If i is even, nums[i] <= nums[i+1]
If i is odd,  nums[i] >= nums[i+1]
Traverse the array, and fix the ordering by swapping unmatched pairs.

Proof:
Suppose sequence [1, 2, ..., i] follows the rule.
If i is odd, we need to prove by swapping, i+1 will follow the rule as well.

If nums[i] >= nums[i+1], it follows the rule.
If nums[i] < nums[i+1], swap nums[i] and nums[i+1]
    Before         After
    e  o  e        e   o  e
   i-1 i i+1      i-1 i+1 i
Because sequence [1, 2, ..., i] follows the rule, nums[i-1] <= num[i], and nums[i] < nums[i+1]. Therefore, nums[i-1] < nums[i+1]. After swapping, the rule sustains.
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i & 1)


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i % 2)


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Scan through nums and swap nums[i] and nums[i+1],
        1) if i is even and nums[i] > nums[i+1];
        2) if i is odd and nums[i] < nums[i+1].
        """
        for i in range(len(nums)-1):
            if not i & 1 and nums[i] > nums[i+1] or i & 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
