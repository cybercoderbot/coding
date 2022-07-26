"""
560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2


Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:

        hmap = defaultdict(int)
        hmap[0] = 1

        res, cumsum = 0, 0
        for n in nums:
            cumsum += n
            res += hmap[cumsum-target]
            hmap[cumsum] += 1

        return res
