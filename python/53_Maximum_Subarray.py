class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 这题是一道经典的dp问题，我们可以很容易的得到其dp方程，假设dp[i]是数组 num [0, i]区间最大的值，那么

        # dp[i] = max(dp[i-1], dp[i-1] + num[i])


        # O(n)的解法，定义两个变量max_sum和cur_sum，其中max_sum保存最终要返回的结果，
        # 即最大的子数组之和，cur_sum初始值为0，每遍历一个数字num，比较cur_sum + n 和n中的较大值存入cur_sum，
        # 然后再把max_sum和cur_sum中的较大值存入max_sum，以此类推直到遍历完整个数组，可得到最大子数组的值存在max_sum中
        
        cur_sum = 0
        max_sum = nums[0]
         
        for n in nums:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(cur_sum, max_sum)
            
        return max_sum
        
        
        
            
