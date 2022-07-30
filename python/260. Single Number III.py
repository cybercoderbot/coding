"""
260. Single Number III
Medium

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)
        return [k for k, v in freq.items() if v == 1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1

        return [x for x in freq if freq[x] == 1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1

        res = []
        for x in freq:
            if freq[x] == 1:
                res.append(x)

        return res
