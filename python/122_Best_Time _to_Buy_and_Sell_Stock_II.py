class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # 这题相对于I来说更加容易，因为不限制交易次数，
        # 我们在第i天买入，如果发现i + 1天比i高，那么就可以累加到利润里面。
        
        if len(prices) <= 1: 
            return 0
        
        profit = 0
        
        for i in range(1,len(prices)):
            profit += max(prices[i] - prices[i-1], 0)
        
        return profit

    
    
    
    
