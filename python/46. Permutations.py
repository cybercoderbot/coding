"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

"""
Approach 1: Backtracking
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

If the first integer to consider has index n that means that the current permutation is done.
Iterate over the integers from index first to index n - 1.
Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
Now backtrack, i.e. swap(nums[first], nums[i]) back."""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Scan through nums and at each position i trigger a recursive call
        with a later element (j) and swap with it.

        Time: O(N!)
        Space: O(N!)
        """

        def backtrack(i):
            """Populate res via backtracking."""
            if i == len(nums):
                res.append(nums.copy())

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        backtrack(i=0)

        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        47. Permutations II, no dupliations allowed
        To exclude duplication, only swap nums[i] with nums[j] when no such value
        has appeared in this position.

        Time: O(N!)
        Space: O(N!)
        """

        def backtrack(i):
            """Populate res via backtracking."""
            if i == len(nums):
                return res.append(nums.copy())

            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    nums[i], nums[j] = nums[j], nums[i]
                    backtrack(i+1)
                    nums[i], nums[j] = nums[j], nums[i]
                    seen.add(nums[j])

        res = []
        backtrack(i=0)

        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution
        """
        res = [[]]
        for x in nums:
            tmp = []
            for pm in res:
                pm.append(x)
                for i in range(len(pm)):
                    pm[i], pm[-1] = pm[-1], pm[i]
                    tmp.append(pm.copy())
                    pm[i], pm[-1] = pm[-1], pm[i]
            res = tmp
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution
        """
        res = [[]]
        for x in nums:
            tmp = []
            seen = set()
            for pm in res:
                pm.append(x)

                for i in range(len(pm)):

                    pm[i], pm[-1] = pm[-1], pm[i]
                    tmp.append(pm.copy())
                    pm[i], pm[-1] = pm[-1], pm[i]
                    seen.add(pm[i])
            if tmp not in seen:
                res = tmp
                seen.append(tmp)
        return res
