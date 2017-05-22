class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # 这道题给我们了一些可用的硬币值，又给了一个钱数，问我们最小能用几个硬币来找零。
        # 根据题目中的例子可知，不是每次都会给全1,2,5的硬币，有时候没有1分硬币，那么有的钱数就没法找零，需要返回-1。
        # 对于求极值问题，我们还是主要考虑动态规划Dynamic Programming来做，我们维护一个一维动态数组dp，
        # 其中dp[i]表示钱数为i时的最小硬币数的找零，递推式为：
        
        # dp[x + c] = min(dp[x] + 1, dp[x + c])
        
        # 其中dp[x]代表凑齐金额x所需的最少硬币数，c为可用的硬币面值
        
        # 初始令dp[0] = 0
        
        # 贪心算法是不正确的，因为有可能会错过全局最优解。

        dp = [0] + [-1]* amount
        
        for x in range(amount):
            if dp[x] <0: continue
            for c in coins:
                if x + c > amount: continue
                if dp[x+c] <0 or dp[x+c] > dp[x]+1:
                    dp[x+c] = dp[x] + 1
                    
        return dp[amount]
        
        
        
        
        
