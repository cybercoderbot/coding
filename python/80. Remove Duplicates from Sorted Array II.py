class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # if not nums: return 
    
        # i = 0
        # for n in nums:
        #     if i < 2 or n > nums[i-2]:
        #         nums[i] = n
        #         i += 1
        # return i
        
        
        # 这道题是之前那道 Remove Duplicates from Sorted Array 有序数组中去除重复项 的延续，
        # 这里允许最多重复两次，那么我们就需要用一个变量count来记录重复的次数（初始化为0），
        # 如果出现过一次重复，则count+=1，那么下次再出现重复，快指针直接前进一步，
        # 如果这时候不是重复的，则count恢复0，由于整个数组是有序的，所以一旦出现不重复的数，
        # 则一定比这个数大，此数之后不会再有重复项
        
        n = len(nums)
        if n<=2: return n
        
        slow, fast = 0, 1
        count = 0
        
        while fast < n:
            if nums[slow] == nums[fast] and count==1:
                fast += 1
            else:
                if nums[slow] == nums[fast]:
                    count += 1
                else:
                    count = 0
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                
        return slow + 1
        
        
        
        
        
        
        
