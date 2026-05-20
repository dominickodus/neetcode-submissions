class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallest = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            smallest = min(smallest, prices[i])

            profit = prices[i] - smallest

            max_profit = max(max_profit, profit)

        return max_profit