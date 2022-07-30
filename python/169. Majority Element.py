"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore majority voting algo"""
        res = vote = 0
        for x in nums:
            if vote == 0:
                res = x
            if x == res:
                vote += 1
            else:
                vote -= 1
        return res


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = freq[res] = -1
        for x in nums:
            freq[x] += 1
            if freq[res] < freq[x]:
                res = x
        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
