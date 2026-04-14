class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            for j in range(i-1, -1,-1):
                sell = prices[i]
                buy = prices[j]
                profit = sell - buy
                max_profit = max(max_profit, profit)
        return max_profit