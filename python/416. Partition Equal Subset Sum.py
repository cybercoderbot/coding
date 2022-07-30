"""
416. Partition Equal Subset Sum
Medium

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
 
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        This is a classic knapsack problem which falls in the area of dynamic programming.

        In this top-down implementation, we define fn(i, x) to return True if there is a subarray summing up to x. Then, the recursive relation is

        fn(i, x) = fn(i+1, x) or fn(i+1, x - nums[i]).
        """

        total = sum(nums)
        if total & 1:
            return False

        @lru_cache(None)
        def dfs(i, x):
            """Return True if possible to find subarray of sum(nums[i:]) = v."""
            if x <= 0:
                return x == 0
            if i == len(nums):
                return False
            return dfs(i+1, x) or dfs(i+1, x - nums[i])

        return dfs(0, total//2)
