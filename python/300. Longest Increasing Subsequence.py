"""
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(N*M) solution. M is the sub[]'s length
        seq = []
        for x in nums:
            i, N = 0, len(seq)
            # update the element to the correct position of the seq.
            while i <= N:
                if i == N:
                    seq.append(x)
                    break
                elif x <= seq[i]:
                    seq[i] = x
                    break
                else:
                    i += 1

        return len(seq)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        O(NlogN) solution with binary search
        """
        def search(s, target):
            left, right = 0, len(s)-1
            while left <= right:
                mid = (left + right)//2
                if s[mid] < target:
                    left = mid + 1
                elif target < s[mid]:
                    right = mid - 1
                else:
                    return mid
            return left

        seq = []
        for x in nums:
            i = search(seq, x)
            if i == len(seq):
                seq.append(x)
            else:
                seq[i] = x
        return len(seq)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time: O(NlogN) 
        """
        vals = []
        for x in nums:
            k = bisect.bisect_left(vals, x)
            if k == len(vals):
                vals.append(x)
            else:
                vals[k] = x
        return len(vals)
