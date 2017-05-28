class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Idea is to work backwards from the last index. Keep track of the smallest index that can 
        # "jump" to the last index. Check whether the current index can jump to this smallest index.


        n = len(nums)
        last = n-1

        for i in range(n-2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0
        
        
        
        
        
