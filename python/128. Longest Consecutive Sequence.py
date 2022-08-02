"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Define a hash set. For each element x, check if x-1 is in the set.
        If not, x is the start of the sequence. Check if x+1, x+2, ... is in the set and 
        update the counter.
        """
        res, vals = 0, set(nums)
        while vals:
            left = right = vals.pop()
            while left-1 in vals:
                vals.remove(left-1)
                left -= 1
            while right+1 in vals:
                vals.remove(right+1)
                right += 1
            res = max(res, right - left + 1)
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the leftmost of the subseq then expand the right side
        Time: O(N), Space: O(N)
        """
        vals = set(nums)
        res = 0
        for x in vals:
            if x - 1 not in vals:
                left = right = x
                while right + 1 in vals:
                    right += 1
                res = max(res, right - left + 1)
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.
        Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.
        """
        vals = set(nums)
        res = 0
        for x in vals:
            if x-1 not in vals:
                y = x + 1
                while y in vals:
                    y += 1
                res = max(res, y-x)
        return res
