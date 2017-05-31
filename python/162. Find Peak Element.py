        
# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
       


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Binary search
        # Choose a number in the middle
        
        if len(nums)==0: return None
        
        left, right = 0, len(nums)-1
    
        
        while left < right:
            mid = (left+right)/2
            if nums[mid] > max(nums[mid+1], nums[mid-1]):
                return mid
                
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        if nums[left] >= nums[right]:
            return left 
        else:
            return right
        
       
