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


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Monotonically decreasing array 
        deq: index of large to small number in nums
        """
        res = []
        deq = collections.deque([])
        for i, x in enumerate(nums):
            # make sure the rightmost val is the smallest
            while deq and nums[deq[-1]] < x:
                deq.pop()

            deq.append(i)

            # make sure the leftmost val is in-bound
            if i - deq[0] >= k:
                deq.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[deq[0]])
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()

        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if deq and i - deq[0] == k:
                deq.popleft()

            while deq:
                # pop useless elements from last/right of the deq
                if nums[deq[-1]] < nums[i]:
                    deq.pop()
                else:
                    break

            deq.append(i)

            # i == k-1 is the beginning of a full window
            res = []
            if i >= k-1:
                res.append(nums[deq[0]])

        return res
