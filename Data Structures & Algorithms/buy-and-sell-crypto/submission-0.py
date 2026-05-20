class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force appraoch

        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):

                profit = prices[j] - prices[i]

                if profit > max_profit:
                    max_profit = profit 

        return max_profit

        