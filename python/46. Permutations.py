"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.


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
Scan through nums and at each position low trigger a recursive call 
with a later element (say i) swapped with it.

"""

"""
Approach 1: Backtracking
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

If the first integer to consider has index n that means that the current permutation is done.
Iterate over the integers from index first to index n - 1.
Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
Now backtrack, i.e. swap(nums[first], nums[i]) back.
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first):
            # if all integers are used up
            if first == n:
                res.append(nums[:])

            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]

                # use next integers to complete the permutations
                backtrack(first+1)

                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack(0)

        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def fn(lo=0):
            """Return permutation of nums starting from index lo"""
            if lo == len(nums)-1:
                yield nums  # base condition
            else:
                yield from fn(lo+1)
                for i in range(lo+1, len(nums)):
                    nums[lo], nums[i] = nums[i], nums[lo]  # swapping
                    yield from fn(lo+1)
                    nums[lo], nums[i] = nums[i], nums[lo]  # swapping back

        yield from fn()


Analysis:
Time complexity O(N!)
Space complexity O(N!)

Compared to the solution when duplication is not allowed.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def fn(i):
            """Populate answer with permutations in backtracking"""
            if i == len(nums):
                ans.append(nums.copy())
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                fn(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        ans = []
        fn(0)
        return ans


Below is Heap's algorithm(1963) which saves one swap in each iteration.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def fn(i):
            """Heap's algorithm (1963)"""
            if i == len(nums):
                ans.append(nums.copy())
            for k in reversed(range(i, len(nums))):
                fn(i+1)
                if (len(nums)-i) & 1:
                    nums[i], nums[-1] = nums[-1], nums[i]
                else:
                    nums[i], nums[k] = nums[k], nums[i]

        ans = []
        fn(0)
        return ans


Approach 3 - - iterative solution


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            tmp = []
            for p in res:
                p.append(n)
                for i in range(len(p)):
                    p[i], p[-1] = p[-1], p[i]
                    tmp.append(p.copy())
                    p[i], p[-1] = p[-1], p[i]
            res = tmp
        return res
