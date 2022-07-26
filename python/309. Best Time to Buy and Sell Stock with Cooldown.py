class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 动态规划（Dynamic Programming）

        # 时间复杂度：O(n)

        # 本题与Best Time to Buy and Sell Stock II 唯一的区别是在卖出股票后需要间隔至少一天才能再次买入。

        # 解法I：引入辅助数组sells和buys

        # sells[i]表示在第i天卖出股票所能获得的最大累积收益
        # buys[i]表示在第i天买入股票所能获得的最大累积收益

        # 初始化令sells[0] = 0，buys[0] = -prices[0]
        # 第i天交易时获得的累计收益只与第i-1天与第i-2天有关

        # 记第i天与第i-1天的价格差：delta = price[i] - price[i-1]

        # 状态转移方程为：

        # buys[i]  = max(sells[i-2] - prices[i], buys[i-1] - delta)
        # sells[i] = max(buys[i-1] + prices[i], sells[i-1] + delta)

        # 上述方程的含义为：
        # 第i天卖出的最大累积收益 = max(第i-1天买入~第i天卖出的最大累积收益, 第i-1天卖出后反悔~改为第i天卖出的最大累积收益)
        # 第i天买入的最大累积收益 = max(第i-2天卖出~第i天买入的最大累积收益, 第i-1天买入后反悔~改为第i天买入的最大累积收益)
        # 而实际上：

        # 第i-1天卖出后反悔，改为第i天卖出 等价于 第i-1天持有股票，第i天再卖出
        # 第i-1天买入后反悔，改为第i天买入 等价于 第i-1天没有股票，第i天再买入
        # 所求的最大收益为max(sells)。显然，卖出股票时才可能获得收益。

        # n = len(prices)
        # if n < 2: return 0
        # buys = [None] * n
        # sells = [None] * n

        # sells[0] = 0
        # buys[0] = -prices[0]

        # for i in range(1, n):
        #     delta = prices[i] - prices[i-1]
        #     sells[i] = max(buys[i-1] + prices[i], sells[i-1] + delta)
        #     buys[i] = max(buys[i-1] - delta, sells[i-2] - prices[i] if i > 1 else None)
        # return max(sells)

        # 解法II：引入辅助数组sells和buys

        # sells[i]表示在第i天 不持有股票所能获得的最大累计收益
        # buys[i] 表示在第i天 持有  股票所能获得的最大累计收益

        # 初始化数组：
        # sells[0] = 0
        # sells[1] = max(0, prices[1] - prices[0])
        # buys[0] = -prices[0]
        # buys[1] = max(-prices[0], -prices[1])

        # 状态转移方程：
        # sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
        # buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])

        # 所求最大收益为sells[-1]

        n = len(prices)
        if n < 2:
            return 0

        buys = [None] * n
        sells = [None] * n

        sells[0] = 0
        sells[1] = max(0, prices[1] - prices[0])
        buys[0] = -prices[0]
        buys[1] = max(-prices[0], -prices[1])

        for i in range(2, n):
            sells[i] = max(sells[i-1], buys[i-1] + prices[i])
            buys[i] = max(buys[i-1], sells[i-2] - prices[i])
        return sells[-1]
