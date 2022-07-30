"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Define a hash set. For each element x, check if x-1 is in the set.

        If not (eg. x is the start of the sequence), 
        progressively check if x+1, x+2, ... is in the set and update the counter.
        If so, do nothing.
        """

        nums = set(nums)
        res = 0
        for x in nums:
            if x-1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y-x)
        return res
