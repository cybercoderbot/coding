"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Monotonically decreasing array 
        queue: index of large to small number in nums
        """

        queue = []
        res = []
        for i, x in enumerate(nums):

            # make sure the rightmost val is the smallest
            while queue and nums[queue[-1]] < x:
                queue.pop()
            queue.append(i)

            # make sure the leftmost val is in-bound
            if i - queue[0] >= k:
                queue.pop(0)

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[queue[0]])
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if queue and i - queue[0] == k:
                queue.popleft()

            while queue:
                # pop useless elements from last/right of the queue
                if nums[queue[-1]] < nums[i]:
                    queue.pop()
                else:
                    break

            queue.append(i)

            # i == k-1 is the beginning of a full window
            res = []
            if i >= k-1:
                res.append(nums[queue[0]])

        return res
