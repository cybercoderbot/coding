class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Binary Search: O(lgn)
        
        if len(nums)==0: return None
        
        left, right = 0, len(nums)-1
    
        # handle condition 3
        while left < right:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
                
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
                
        #handle condition 1 and 2
        return left if nums[left] >= nums[right] else right
