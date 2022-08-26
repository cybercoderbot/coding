"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        N = len(nums1) + len(nums2)
        if N % 2:
            return self.findKth(nums1, nums2, N // 2)
        else:
            x = self.findKth(nums1, nums2, N // 2)
            y = self.findKth(nums1, nums2, N // 2 - 1)
            return (x + y) / 2.0

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        i, j = len(nums1) // 2, len(nums2) // 2

        if i + j < k:
            # if nums1's median < nums2's median, nums2's first half doesn't include k
            if nums1[i] > nums2[j]:
                return self.findKth(nums1, nums2[j+1:], k-j-1)
            else:
                return self.findKth(nums1[i+1:], nums2, k-i-1)

        else:
            # if nums1's median > nums2's, nums1's second half doesn't include k
            if nums1[i] > nums2[j]:
                return self.findKth(nums1[:i], nums2, k)
            else:
                return self.findKth(nums1, nums2[:j], k)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search. Call 2 times findKth and k is about half of (M+N). 
        Every time call findKth can reduce the scale k to its half. 
        So the time complexity is O(log(M+N)).
        """
        N = len(nums1)+len(nums2)

        if N % 2:
            return self.findKth(nums1, nums2, N//2)
        else:
            x = self.findKth(nums1, nums2, N//2-1)
            y = self.findKth(nums1, nums2, N//2)
            return (x + y) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            return nums2[k]
        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])

        i = min(len(nums1)-1, k//2)
        j = min(len(nums2)-1, k-i)

        if nums1[i] > nums2[j]:
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)
