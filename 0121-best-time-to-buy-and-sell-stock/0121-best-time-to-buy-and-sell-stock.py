class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_prices = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy_prices:
                buy_prices = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - buy_prices)
        return max_profit 
        