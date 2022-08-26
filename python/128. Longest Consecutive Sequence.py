"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

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
        numSet = set(nums)
        longest = 0
        for x in nums:
            if x - 1 not in numSet:
                length = 1
                while x + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the leftmost of the subseq then expand the right side
        Time: O(N), Space: O(N)
        """
        vals = set(nums)
        res = 0
        for x in vals:
            if x - 1 not in vals:
                left = right = x
                while right + 1 in vals:
                    right += 1
                res = max(res, right - left + 1)
        return res
