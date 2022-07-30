"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], k = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], k = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], k = 0
Output: 3
"""


"""
Keep track of the max and min in two deques.
"""


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        i = 0
        minq, maxq = [], []

        for x in nums:
            while minq and minq[-1] > x:
                minq.pop()
            while maxq and maxq[-1] < x:
                maxq.pop()

            minq.append(x)
            maxq.append(x)

            if maxq[0] - minq[0] > k:
                if nums[i] == minq[0]:
                    minq.pop(0)
                if nums[i] == maxq[0]:
                    maxq.pop(0)
                i += 1

        return len(nums) - i


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        lo = i = ans = 0
        minq, maxq = [], []  # (index, value)

        while i < len(nums):
            while minq and minq[-1][1] >= nums[i]:
                minq.pop()
            while maxq and maxq[-1][1] <= nums[i]:
                maxq.pop()
            minq.append((i, nums[i]))
            maxq.append((i, nums[i]))

            if maxq[0][1] - minq[0][1] > k:
                lo += 1
                if lo > minq[0][0]:
                    minq.pop(0)
                if lo > maxq[0][0]:
                    maxq.pop(0)
            else:
                ans = max(ans, i - lo + 1)
                i += 1
        return ans


# A more efficient implementation is given by @ lee215 in this thread.
