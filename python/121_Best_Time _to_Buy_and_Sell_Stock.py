class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # 这是卖股票的第一个题目，根据题意我们知道只能进行一次交易，但需要获得最大的利润，
        # 所以我们需要在最低价买入，最高价卖出，当然买入一定要在卖出之前。

        # 对于这一题，我们只需要遍历一次数组，通过一个变量记录当前最低价格，
        # 同时算出此次交易利润，并与当前最大值比较就可以了。
        
        if len(prices) <=1: return 0
        
        pmin = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-pmin)
            profit = max(profit, 0)
            pmin = min(pmin, prices[i])
        return profit
    
    
    
    
        
