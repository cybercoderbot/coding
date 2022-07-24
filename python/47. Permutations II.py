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

"""
Scan through nums and at each position lo trigger a recursive call with a later element 
(say i) swapped with it. To exclude duplication, only swap nums[i] with nums[lo] when no such 
value has appeared in this position.
"""




from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity O(N!)
        Space complexity O(N!)
        """

        def backtrack(left):
            """Populate res via backtracking."""
            if left == len(nums):
                return res.append(nums.copy())

            seen = set()
            for right in range(left, len(nums)):
                if nums[right] not in seen:
                    nums[left], nums[right] = nums[right], nums[left]
                    backtrack(left+1)
                    nums[left], nums[right] = nums[right], nums[left]
                    seen.add(nums[right])

        res = []
        backtrack(0)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(num, perm):
            if not num:
                res.append(perm[:])

            for i in range(len(num)):
                string = ",".join([str(c) for c in perm+[num[i]]])
                if string not in visited:
                    perm.append(num[i])
                    visited.add(string)
                    backtrack(num[:i]+num[i+1:], perm)
                    perm.pop()

        backtrack(nums, [])

        return res
