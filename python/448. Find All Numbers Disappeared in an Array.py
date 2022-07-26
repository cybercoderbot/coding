"""
448. Find All Numbers Disappeared in an Array
Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Solution:
To achive O(1) space usage, we have to mark the input array so that the info is preserved. There are many ways to achieve this. For example, one could simply mark the cell pointed by value in another cell negative, so that the index corresponding to cell with positive numbers are missing from the input, i.e. negative encoding.
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Use nums as index -> if seen, set num[n-1] -> negative
        """
        for x in nums:
            n = abs(x)
            nums[n-1] = -abs(nums[n-1])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            while x:
                nums[x-1], x = 0, nums[x-1]
        return [i+1 for i, x in enumerate(nums) if x > 0]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            nums[abs(x)-1] = -abs(nums[abs(x)-1])
        return [i+1 for i, x in enumerate(nums) if x > 0]


"""
442. Find All Duplicates in an Array
Medium

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Solution
O(1) space not including the input and output variables

The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. We do this by making elements at certain indexes negative. 
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        O(n) time 
        O(1) space
        """
        res = []
        for x in nums:
            n = abs(x)
            # first seen, set to negative
            if nums[n-1] > 0:
                nums[n-1] *= -1
            else:
                # negative ->  seen before -> add to res
                res.append(n)

        return res
