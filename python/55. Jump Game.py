"""
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        """
        Idea is to work backwards from the last index.
        Keep track of the smallest index that can "jump" to the last index.
        Check whether the current index can jump to this smallest index.
        """

        N = len(nums)
        last = N-1

        for i in range(N-2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        longest = 0

        i, N = 0, len(nums)
        while i <= longest:
            longest = max(longest, i + nums[i])
            if longest >= N - 1:
                return True
            i += 1

        return False
