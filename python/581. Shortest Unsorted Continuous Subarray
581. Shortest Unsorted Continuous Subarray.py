"""
581. Shortest Unsorted Continuous Subarray
Medium

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0
"""


"""
To find the upper bound of the unsorted subarray, one needs to loop through the list forward and keep track of the running maximum. The last position where the element value doesn't match the running maximum is the upper bound(hi).
Similarly, to find the lower bound, simply loop through the list backward(starting from hi), and the last position where the current element doens't match the running minimum marks the lower bound(lo).

"""


class Solution(object):
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Sort the list and check if it's still the same number in the list.
        """
        pairs = zip(nums, sorted(nums))
        res = [i for (i, (a, b)) in enumerate(pairs) if a != b]
        return res[-1] - res[0] + 1 if res else 0


class Solution(object):
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        sort = sorted(nums)
        left = right = -1

        for i in range(len(nums)):
            if nums[i] != sort[i]:
                if left == -1:
                    left = i
                right = i

        if left == right:
            return 0
        else:
            return right - left + 1


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = right = 0
        N = len(nums)

        mmax = -inf
        for i in range(N):
            mmax = max(mmax, nums[i])
            if nums[i] < mmax:
                right = i+1

        mmin = inf
        for i in range(right-1, -1, -1):  # lo <= hi
            mmin = min(mmin, nums[i])
            if nums[i] > mmin:
                left = i

        return right - left
