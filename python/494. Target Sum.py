"""
494. Target Sum
Medium

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {0: 1}
        for x in nums:
            d = defaultdict(int)
            for sm, n in memo.items():
                d[sm+x] += n
                d[sm-x] += n
            memo = d
        return memo[target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = collections.Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y+x] += count[y]
                step[y-x] += count[y]
            count = step
        return count[target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def fn(i, x):
            """Return number of ways to assign symbols to sum nums[i:] to t."""
            if i == len(nums):
                return x == 0
            return fn(i+1, x-nums[i]) + fn(i+1, x+nums[i])

        return fn(0, target)
