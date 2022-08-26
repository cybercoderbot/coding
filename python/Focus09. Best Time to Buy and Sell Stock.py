"""
The buy low & sell high approach could be used to solve all problems in this series.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock (1 transaction)
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
        """
        buy, sell = inf, 0
        for x in prices:
            buy = min(buy, x)
            sell = max(sell, x - buy)
        return sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock
        """
        res = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            res = max(res, prices[right] - prices[left])
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        122. Best Time to Buy and Sell Stock II (Unlimited transactions)
        """
        buy, sell = inf, 0
        for x in prices:
            buy = min(buy, x - sell)
            sell = max(sell, x - buy)
        return sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        123. Best Time to Buy and Sell Stock III (At most 2 transactions)
        """
        buy, sell = [inf] * 2, [0] * 2

        for x in prices:
            for i in range(2):
                if i:
                    buy[i] = min(buy[i], x - sell[i-1])
                else:
                    buy[i] = min(buy[i], x)

                sell[i] = max(sell[i], x - buy[i])

        return sell[1]


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        188. Best Time to Buy and Sell Stock IV (At most k transactions)
        """
        if k >= len(prices)//2:
            res = 0
            for i in range(1, len(prices)):
                res += max(0, prices[i] - prices[i-1])
            return res

        buy, sell = [inf] * k, [0] * k
        for x in prices:
            for i in range(k):
                if i:
                    buy[i] = min(buy[i], x - sell[i-1])
                else:
                    buy[i] = min(buy[i], x)
                sell[i] = max(sell[i], x - buy[i])

        return sell[-1] if k and prices else 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        309. Best Time to Buy and Sell Stock with Cooldown
        """
        buy, cooldown, sell = inf, 0, 0
        for x in prices:
            buy = min(buy, x - cooldown)
            cooldown = sell
            sell = max(sell, x - buy)
        return sell


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        714. Best Time to Buy and Sell Stock with Transaction Fee
        """
        buy, sell = inf, 0
        for x in prices:
            buy = min(buy, x - sell)
            sell = max(sell, x - buy - fee)
        return sell
