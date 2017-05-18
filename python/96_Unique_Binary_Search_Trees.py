class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 解题思路：这题从数学上讲，其实是Catalan number.
        # 解题技巧：一般来说求数量，要首先想到使用Dynamic Programming，
        # 而如果是不只是数量，还要把所有的树都枚举出来，就要使用DFS来遍历决策树

        # 大部分动态规划的难点都是求状态转移方程。那么如何去求这个问题的formulation呢？
        # n=0时，为空树，那么dp[0]=1; 
        # n=1时，显然也是1，dp[1]=1；
        # n=2时，dp[2]=2; 
        # 对于n>2时，dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+......+dp[n-1]*dp[0]
        
        dp = [1,1,2]
        if n<=2: return dp[n]
        
        for i in range(3,n+1):
            for j in range(1,i+1):
                dp[i] = dp[j-1] * dp[i-1]
        return dp[n]
                


　　　　　
