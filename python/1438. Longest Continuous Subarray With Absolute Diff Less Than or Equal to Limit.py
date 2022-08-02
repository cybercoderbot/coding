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


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        """
        The idea is to use sliding window and 2 monotonic queues to keep track of the window max and window min.

        In the beginning, we set both left pointer "left" and right pointer "right" at index 0. 
        We keep moving right forward until the max absolute difference within the window exceeds the limit. Then, we move forward left until the max absolute difference falls back within the limit.

        We know that:
        max absolute difference = max value within the window - min value within the window
        The tricky part is to get the max and min value within a window. 
        To do so, we can use two monotonic queues: minq and maxq.
        minq is monotonically increasing and maxq is monotonically decreasing. In this way, minq[0] will be the min value within a window and maxq[0] will be the max value within the window.

        We can store index in minq and maxq to get rid of out-of-window numbers more easily. So we will use nums[minq[0]] instead of minq[0] to get numbers. The concept stays the same.

        Time: O(N), Space: O(N)
        """
        minq, maxq = [], []  # (index, value)

        left = right = res = 0
        while right < len(nums):
            while minq and minq[-1][1] >= nums[right]:
                minq.pop()
            while maxq and maxq[-1][1] <= nums[right]:
                maxq.pop()
            minq.append((right, nums[right]))
            maxq.append((right, nums[right]))

            if maxq[0][1] - minq[0][1] > k:
                left += 1
                if left > minq[0][0]:
                    minq.pop(0)
                if left > maxq[0][0]:
                    maxq.pop(0)
            else:
                res = max(res, right - left + 1)
                right += 1
        return res


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        """
        Keep track of the max and min in two deques.
        """
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
