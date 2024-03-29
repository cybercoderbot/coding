"""
215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(NlogN) time
        return sorted(nums)[-k]

    def findKthLargest1(self, nums, k):
        # O(NlogN) time
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest4(self, nums, k):
        """
        Min Heap, O(k+(N-k)logk) time
        """
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in xrange(k):
            for j in xrange(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    # exchange elements, time consuming
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums)-k]

    # O(nk) time, selection sort idea
    def findKthLargest3(self, nums, k):
        for i in xrange(len(nums), len(nums)-k, -1):
            tmp = 0
            for j in xrange(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return nums[len(nums)-k]

    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapify(heap)
        for x in nums[k:]:
            heappushpop(heap, x)
        return heap[0]

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
