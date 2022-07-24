"""
45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

"""


"""
The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
right = max(i + nums[i] for i in range(left, right + 1)


"""


class Solution:

    def jump(self, nums):
        if len(nums) <= 1:
            return 0

        left, right = 0, nums[0]
        res = 1

        while right < len(nums) - 1:
            res += 1
            farthest = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, farthest

        return res


class Solution:
    def jump(self, nums: List[int]) -> int:
        # [0, end) represents the range of indeces we can reach with count steps
        # [start, end) represents the range of indeces that we can reach but have never calculated

        start, end = 0, 1

        res = 0
        while end < len(nums):
            MAX = max(nums[i]+i+1 for i in range(start, end))
            start, end = end, MAX
            res += 1

        return res
