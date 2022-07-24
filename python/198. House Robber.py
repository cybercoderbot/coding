"""
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


"""
Based on the recursive formula:

f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max(f(k-2) + nums[k], f(k-1))
"""


class Solution:

    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        N = len(nums)

        dp = [0] * (N + 1)
        dp[N], dp[N-1] = 0, nums[N-1]

        for i in range(N-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])

        return dp[0]


class Solution:
    def rob(self, nums: List[int]) -> int:

        pre, now = 0, 0
        for i in nums:
            pre, now = now, max(pre + i, now)

        return now
