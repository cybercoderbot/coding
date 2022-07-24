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

# This is a classic knapsack problem which falls in the regime of dynamic programming.

# In this top-down implementation, we define fn(i, v) to return True if there is a subarray summing up to v in nums[i:]. Then, the recursive relation is

# fn(i, v) = fn(i+1, v) or fn(i+1, v - nums[i]).


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        @lru_cache(None)
        def dfs(i, v):
            """Return True if possible to find subarray of nums[i:] summing to v."""
            if v <= 0:
                return v == 0
            if i == len(nums):
                return False
            return dfs(i+1, v) or dfs(i+1, v - nums[i])

        return dfs(0, total//2)
