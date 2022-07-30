"""
922. Sort Array By Parity II
Easy

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]

Even & odd indices
maintain two indices "even" and "odd" which start at 0 and 1 spectively
loop through elements in array
if element is of odd parity, copy it to position of "odd" index and increase odd by two
if element is of even parity, copy it to positon of "even" index and increase even by two.

"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        index = [0, 1]  # even & odd indices
        for x in nums:
            res[index[x % 2]] = x
            index[x % 2] += 2
        return res


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        An alternative implementation that updates nums in place.
        """
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if not nums[i] & 1:
                i += 2
            elif nums[j] & 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums
