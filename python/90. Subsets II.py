"""
78. Subsets
Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

"""
Approach 1 - recursive
Use one stack to keep track of elements in nums.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking
        Time: (N * 2^N) to generate all subsets and then copy them into output list.

        Space: O(N). We are using O(N) space to maintain cand, and are modifying cand in-place with backtracking. Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.
        """

        def backtrack(i):
            """Populate res using a stack (cand)"""
            if len(nums) == i:
                return res.append(cand.copy())

            backtrack(i+1)
            cand.append(nums[i])
            backtrack(i+1)
            cand.pop()

            return

        res, cand = [], []
        backtrack(0)

        return res


"""
Approach 2 - list comprehension 

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:  Cascading

        Let's start from empty subset in output list. At each step one takes new integer into consideration and generates new subsets from the existing ones.

        Time: O(N * 2^N) to generate all subsets and then copy them into output list.
        Space: O(N * 2^N). This is exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.
        """
        res = [[]]
        for n in nums:
            res += [r + [n] for r in res]
        return res


"""
90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


"""
This problem is an extension of 78. Subsets. The original problem can be either solved using iterative or recursive implementation per this thread. But for this problem, the recursive solution is easier to implement.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i):
            """Populate res using a stack (cand)"""
            if len(nums) == i:
                return res.append(cand.copy())

            backtrack(i+1)
            cand.append(nums[i])
            backtrack(i+1)
            cand.pop()

            return

        res, cand = [], []
        backtrack(0)

        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i):
            """Populate res using a stack (cand)"""
            if len(nums) == i:
                return res.append(cand.copy())

            if not cand or nums[i] != cand[-1]:
                backtrack(i+1)

            cand.append(nums[i])
            backtrack(i+1)
            cand.pop()
            return

        nums.sort()
        res, cand = [], []
        backtrack(0)

        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution
        """
        nums.sort()
        res = [[]]
        size = 0
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                j = size
            else:
                j = 0
            size = len(res)
            while j < size:
                res.append(res[j] + [nums[i]])
                j += 1
        return res
