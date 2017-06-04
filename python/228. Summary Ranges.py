class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        # 这道题给定我们一个有序数组，让我们总结区间，具体来说就是让我们找出连续的序列，
        # 然后首尾两个数字之间用个“->"来连接，那么我只需遍历一遍数组即可，每次检查下一个数
        # 是不是递增的，如果是，则继续往下遍历，如果不是了，我们还要判断此时是一个数还是一个序列，
        # 一个数直接存入结果，序列的话要存入首尾数字和箭头“->"。我们需要两个变量i和d，其中i是连续序列
        # 起始数字的位置，d是连续数列的长度，当d为1时，说明只有一个数字，若大于1，则是一个连续序列
        
        # i, n = 0, len(nums)
        # ans = []
        # while i < n:
        #     d = 1
        #     while i+d<n and nums[i+d] - nums[i] == d:
        #         d += 1
        #     if d <= 1:
        #         s = str(nums[i])
        #     else:
        #         s = str(nums[i]) + "->" + str(nums[i+d-1])
        #     ans.append(s)
        #     i += d
        # return ans
        
        i, n = 0, len(nums)
        ans = []
        while i < n:
            i0, s = i, str(nums[i])
            while i+1 < n and nums[i+1] - nums[i] == 1:
                i += 1
            if i > i0:
                s += "->" + str(nums[i])
            ans.append(s)
            i += 1
        return ans
        
        
