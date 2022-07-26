"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """

        # 这是卖股票的第一个题目，根据题意我们知道只能进行一次交易，但需要获得最大的利润，
        # 所以我们需要在最低价买入，最高价卖出，当然买入一定要在卖出之前。

        # 对于这一题，我们只需要遍历一次数组，通过一个变量记录当前最低价格，
        # 同时算出此次交易利润，并与当前最大值比较就可以了。

        low = float('inf')
        res = 0
        for cur in prices:
            low = min(low, cur)
            res = max(res, cur - low)

        return res
