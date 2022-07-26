"""
162. Find Peak Element
Medium

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Solution: Binary search O(log n)

Elaboration:
If an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, because the elements on its right is either

    1. always increasing  -> the right-most element is the peak
    2. always decreasing  -> the left-most element is the peak
    3. first increasing then decreasing -> the pivot point is the peak
    4. first decreasing then increasing -> the left-most element is the peak

    Therefore, we can find the peak only on its right elements( cut the array to half)

    The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.



Conditions:
1. array length is 1  -> return the only index
2. array length is 2  -> return the bigger number's index
3. array length is bigger than 2 ->
   (1) find mid, compare it with its left and right neighbors
   (2) return mid if nums[mid] greater than both neighbors
   (3) take the right half array if nums[mid] smaller than right neighbor
   (4) otherwise, take the left half

Run time: O(logn)
Memory: constant
Test cases:
     [1]
     [1,2]
     [2,1]
     [1,2,3]
     [3,2,1]
     [2,1,3]

"""


class Solution(object):
    def findPeakElement(self, nums: List[int]): -> int:
        """
        Binary search
        Choose a number in the middle
        """

        if not nums:
            return 0

        left, right = 0, len(nums)-1

        # condition 3
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > max(nums[mid+1], nums[mid-1]):
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        # condition 1 and 2
        if nums[left] >= nums[right]:
            return left
        else:
            return right
