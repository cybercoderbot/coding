"""
137. Single Number II
Medium

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        return next(k for k, v in freq.items() if v == 1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums)) // 2


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        return sorted(d, key=d.get)[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next(n for n in nums if nums.count(n) == 1)
