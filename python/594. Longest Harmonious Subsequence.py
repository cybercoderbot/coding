"""
594. Longest Harmonious Subsequence
Easy

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.


Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
"""


"""
Get the frequency table of nums.
Check the elements in nums and if x+1 is in freq, update res.

"""


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Time complexity O(N)
        Space complexity O(N)
        """
        freq = Counter(nums)

        res = 0
        for x in nums:
            if x + 1 in freq:
                res = max(res, freq[x] + freq[x+1])
        return res
