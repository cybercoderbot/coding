"""
39. Combination Sum
Medium

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


"""
Approach 1 -- backtracking
Keep track of a list of existing numbers and residual. When residual drops to 0, add list to answer.

"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time complexity O(K^N), where K = target/min(candidates) and N = len(candidates)
        Space complexity O(K^N)
        """

        # For faster speed
        candidates.sort()

        def backtrack(i, x):
            """Populate res via backtracking."""
            if x < 0:
                return
            if x == 0:
                return res.append(stack[:])
            for j in range(i, len(candidates)):
                if x < candidates[j]:
                    break
                stack.append(candidates[j])
                backtrack(j, x-candidates[j])
                stack.pop()

        res, stack = [], []
        backtrack(0, target)
        return res


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
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of the 
range [1, n].

You may return the answer in any order.

 
Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Backtracking"""

        def backtrack(i):
            """Populate res using a stack"""
            if len(stack) == k:
                return res.append(stack.copy())
            if len(stack) + n - i < k:
                return
            for j in range(i+1, n+1):
                stack.append(j)
                backtrack(j)
                stack.pop()

        res, stack = [], []
        backtrack(0)

        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Iterative implementation"""

        res, stack = [], []
        x = 1
        while True:
            if len(stack) == k:
                res.append(stack[:])
            if len(stack) == k or k - len(stack) > n - x + 1:
                if not stack:
                    break
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        return res


"""
216. Combination Sum III
Medium

3940

89

Add to List

Share
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

"""

"""
This problem is in the sequal of combination sum. 
Such problems are typically solved via "backtracking" but there could be many 
implemenations each with pros and cons. My preferred means of solving such problems 
is to recursively explore the solution space while maintaining a stack with elements 
that have been collected so far.

While condition is met, we save a copy of the stack in the answer. Upon fully exploring 
the solution space, we return anwser to the calling function. Time complexity of such 
algo is typically exponential while space complexity could be exponential as well.
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrack(n, i):
            """Populate res with a stack."""
            if n < 0 or len(stack) > k:
                return
            if n == 0 and len(stack) == k:
                return res.append(stack.copy())
            for j in range(i, 10):
                stack.append(j)
                backtrack(n-j, j+1)
                stack.pop()

        res, stack = [], []
        backtrack(n, 1)

        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """DP"""
        dp = [[] for _ in range(n+1)]
        dp[0].append([])

        for x in range(1, 10):
            for i in range(n-1, -1, -1):
                if i+x <= n:
                    for seq in dp[i]:
                        dp[i+x].append(seq + [x])

        return [seq for seq in dp[-1] if len(seq) == k]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        ad-hoc
        """
        res, stack = [], []
        x = 1
        while True:
            if len(stack) == k and sum(stack) == n:
                res.append(stack.copy())
            if len(stack) == k or k - len(stack) > 10 - x:
                if not stack:
                    break
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        return res


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
