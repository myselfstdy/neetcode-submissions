class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        maxi_profit = float('-inf')
        mini = prices[0]
        for i in range(1,len(prices)):
            mini = min(mini,  prices[i])
            profit = abs(prices[i] - mini)
            if profit > maxi_profit:
                maxi_profit = profit
        return maxi_profit

        