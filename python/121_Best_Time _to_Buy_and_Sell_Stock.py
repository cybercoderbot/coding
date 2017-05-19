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


        if len(prices)<=1: return 0
        
        p_min = prices[0]
        profit = max(0, prices[1] - prices[0])
        
        for p_cur in prices[1:]:
            profit = max(profit, p_cur - p_min)
            profix = max(profit, 0)
            p_min = min(p_cur, p_min)
        
        return profit
