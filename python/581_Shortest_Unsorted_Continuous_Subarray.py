class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序（Sort）

        # 对数组nums排序，记排序后的数组为nsorted，数组长度为n
        
        # 令left = right = -1
        
        # 从0到n-1枚举i，记满足nums[i] != nsorted[i]的最小i值为s，最大i值为e
        
        # 则当 left != right 时，所求最短连续子数组为nums[s .. e] 
        
        # 否则，所求子数组为空

        
        nsorted = sorted(nums)
        left = right = -1
        for i in range(len(nums)):
            if nums[i] != nsorted[i]:
                if left == -1: 
                    left = i
                right = i
                
        if left == right:
            return 0
        else:
            return right - left + 1




