class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        39. Combination Sum
        The same number may be chosen from candidates an unlimited number of times
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        Approach 1: backtracking
        Keep track of a list of existing numbers and residual. 
        When residual drops to 0, add list to answer.

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
            return

        res, stack = [], []

        backtrack(i=0, x=target)

        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        39. Combination Sum
        The same number may be chosen from candidates an unlimited number of times
        """
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for x in candidates:
            for i in range(target):
                if i+x <= target:
                    for seq in dp[i]:
                        dp[i+x].append(seq + [x])
        return dp[-1]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        77. Combinations
        Given two integers n and k, 
        return all possible combinations of k numbers out of the range [1, n].

        Backtracking
        """

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

        backtrack(i=0)

        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        77. Combinations
        Iterative implementation
        """

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


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        216. Combination Sum III
        Find all valid combinations of k numbers that sum up to n such that:

        Each number is used at most once.
        The list must not contain the same combination twice.
        """

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
        """
        216. Combination Sum III
        DP
        """
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
        216. Combination Sum III. Ad-hoc
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


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        377. Combination Sum IV
        Return the number of possible combinations that add up to target.
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
        377. Combination Sum IV
        Return the number of possible combinations that add up to target.
        The bottom-up dp is given below using an array.
        """

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target):
            for x in nums:
                if i+x <= target:
                    dp[i+x] += dp[i]

        return dp[-1]
