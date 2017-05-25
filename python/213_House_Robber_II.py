class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 这道题是之前那道 House Robber 打家劫舍的拓展，现在房子排成了一个圆圈，则如果抢了第一家，
        # 就不能抢最后一家，因为首尾相连了，所以第一家和最后一家只能抢其中的一家，或者都不抢，
        # 那我们这里变通一下，如果我们把第一家和最后一家分别去掉，各算一遍能抢的最大值，然后比较
        # 两个值取其中较大的一个即为所求。那我们只需参考之前的House Robber 打家劫舍中的解题方法，
        # 然后调用两边取较大值
        
        if not nums: return 0
        if len(nums)==1: return nums[0]
        return max(self.rob2(nums[1:]), self.rob2(nums[:-1]))
        
    def rob2(self, nums):
        if not nums: return 0
        if len(nums)==1: return nums[0]
        
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]
        
