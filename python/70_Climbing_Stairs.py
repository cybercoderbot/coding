class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 解题思路：
        # 问题的本质是求 Fibonacci Sequence
        # 假设梯子有n层，那么如何爬到第n层呢，因为每次只能怕1或2步，那么爬到第n层的方法要么是从第n-1层一步上来的，
        # 要不就是从n-2层2步上来的，所以DP公式非常容易的就得出了：dp[n] = dp[n-1] + dp[n-2]
       
        if n==0: return 1
        if n <= 2: return n
        
        dp = [0]* (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        
        
        
        
