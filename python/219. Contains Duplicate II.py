"""
219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. Contains Duplicate
        Return true if any value appears more than once
        """
        return len(set(nums)) < len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. Contains Duplicate
        Return true if any value appears more than once
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        219. Contains Duplicate at distance k
        Return true if any value appears more than once
        """
        seen = dict()
        for i, x in enumerate(nums):
            if x in seen and i - seen[x] <= k:
                return True
            seen[x] = i
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        220. Contains Duplicate at distance k within delta t
        Put numbers in a given range into bucket (k). Bucketing numbers properly, this becomes almost identical to 219, except that numbers in adjacent buckets need to be check as well.
        """
        if t < 0:
            return False

        seen = {}
        for i, x in enumerate(nums):
            b = x // (t+1)
            if b in seen and i-seen[b][0] <= k:
                return True
            for y in b-1, b+1:
                if y in seen and i-seen[y][0] <= k and abs(x-seen[y][1]) <= t:
                    return True
            seen[b] = (i, x)
        return False
