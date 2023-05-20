class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            profit = max(profit, prices[i] - minprice)
        return profit
