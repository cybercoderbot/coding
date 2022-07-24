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
Output: [[1]]"""


"""
Scan through nums and at each position lo trigger a recursive call with a later element 
(say i) swapped with it.

Time complexity O(N!)
Space complexity O(N!)
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Duplication allowed.
        """

        def backtrack(i):
            """Populate res in backtrack"""
            if i == len(nums):
                res.append(nums.copy())

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        backtrack(0)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Duplication NOT allowed.
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
        backtrack(0)
        return res


"""
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.


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


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Duplication NOT allowed.
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
        backtrack(0)
        return res


"""
266. Palindrome Permutation
Easy

Given a string s, return true if a permutation of the string could form a palindrome.

Example 1:
Input: s = "code"
Output: false

Example 2:
Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        freq = collections.Counter(s)
        return sum([x & 1 for x in freq.values()]) <= 1


"""
267. Palindrome Permutation II
Medium

Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, 
return an empty list.

 
Example 1:
Input: s = "aabb"
Output: ["abba","baab"]

Example 2:
Input: s = "abc"
Output: []

"""


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        freq = Counter(s)

        nodd = sum(x & 1 for x in freq.values())
        if nodd > 1:
            return []

        res = []
        vals, mid = [], ""
        for k, v in freq.items():
            vals.extend([k] * (v//2))
            if v & 1:
                mid = k

        def backtrack(i):
            """Permutation without duplicates."""
            if i == len(vals):
                res.append("".join(vals) + mid + "".join(vals[::-1]))

            seen = set()
            for j in range(i, len(vals)):
                if vals[j] not in seen:
                    seen.add(vals[j])
                    vals[i], vals[j] = vals[j], vals[i]
                    backtrack(i+1)
                    vals[i], vals[j] = vals[j], vals[i]

        backtrack(0)

        return res
