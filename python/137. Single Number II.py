"""
137. Single Number II
Medium

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it. Find a solution in O(N) time and O(1) space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(1) space"""
        return (sum(set(nums))*3 - sum(nums)) // 2


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(N) space"""
        freq = collections.Counter(nums)
        return next(k for k, v in freq.items() if v == 1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(N) space"""
        for x in nums:
            if nums.count(x) == 1:
                return x


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(N) space"""
        return collections.Counter(nums).most_common()[-1][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(N) space"""
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        return next(k for k, v in freq.items() if v == 1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(N) space"""
        d = Counter(nums)
        return sorted(d, key=d.get)[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """O(N) time, O(N) space"""
        return next(x for x in nums if nums.count(x) == 1)
