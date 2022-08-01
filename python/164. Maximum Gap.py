"""
164. Maximum Gap
Hard

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """Bucket sort"""
        low, high = min(nums), max(nums)
        N = len(nums)
        if N <= 2 or high == low:
            return high - low

        buckets = defaultdict(list)
        for x in nums:
            if x == high:
                i = N-2
            else:
                i = (x - low)*(N-1)//(high-low)
            buckets[i].append(x)

        res = []
        for i in range(N-1):
            if not buckets[i]:
                continue
            res.append([min(buckets[i]), max(buckets[i])])

        return max(y[0]-x[1] for x, y in zip(res[:-1], res[1:]))
