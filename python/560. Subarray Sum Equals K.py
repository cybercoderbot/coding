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
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        N = len(nums)

        for i in range(N):
            cumsum = nums[i]
            if cumsum == k:
                res += 1
            for j in range(i+1, N):
                cumsum += nums[j]
                if cumsum == k:
                    res += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        To count all subarrays sum up to k

        we can count all possible sums iterating through nums
        and use

            sum[i:j] = sum[:j] - sum[:i] = k

            sum[:i] = sum[:j] - k

        to check if sum[i:j] == k, and with the count of sums before j
        we can add count[sum[:j] - k] to the final count at each j

        we will want to initiate count[0] to 1, so that sum[:j] == k can be counted
        """

        freq = defaultdict(int)
        freq[0] = 1

        res, cumsum = 0, 0
        for x in nums:
            cumsum += x
            res += freq[cumsum-k]
            freq[cumsum] += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        To count all subarrays sum up to k

        we can count all possible sums iterating through nums
        and use

            sum[i:j] = sum[:j] - sum[:i] = k

            sum[:i] = sum[:j] - k

        to check if sum[i:j] == k, and with the count of sums before j
        we can add count[sum[:j] - k] to the final count at each j

        we will want to initiate count[0] to 1, so that sum[:j] == k can be counted
        """

        freq = defaultdict(int)

        res, cumsum = 0, 0
        for x in [0] + nums:
            cumsum += x
            res += freq[cumsum-k]
            freq[cumsum] += 1
        return res
