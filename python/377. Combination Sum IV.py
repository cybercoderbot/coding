"""
39. Combination Sum
Medium

12175

255

Add to List

Share
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for x in candidates:
            for i in range(target):
                if i+x <= target:
                    for seq in dp[i]:
                        dp[i+x].append(seq + [x])
        return dp[-1]


"""
377. Combination Sum IV
Medium

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
"""

"""
Even though this problem is titled "combination sum iv" it is not consistent with the previous three problems in the series. While combination sum i, ii, iii are solved via backtracking, this is a dynamic programming problem.


"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        The top-down dp is given below through the definition of dp().
        """

        @lru_cache(None)
        def dp(n):
            """Return number of combinations adding up to n."""
            if n <= 0:
                return int(n == 0)
            return sum(dp(n-x) for x in nums)

        return dp(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        The bottom-up dp is given below using an array.
        """

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target):
            for x in nums:
                if i+x <= target:
                    dp[i+x] += dp[i]

        return dp[-1]
