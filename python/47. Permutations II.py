"""
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        47. Permutations II, no dupliations allowed
        Scan through nums and at each position i trigger a recursive call with a 
        later element (j) swapped with it
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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(num, perm):
            if not num:
                res.append(perm[:])

            for i in range(len(num)):
                string = ",".join([str(c) for c in perm + [num[i]]])
                if string not in visited:
                    perm.append(num[i])
                    visited.add(string)
                    backtrack(num[:i] + num[i+1:], perm)
                    perm.pop()

        backtrack(nums, perm=[])

        return res
