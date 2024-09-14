class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxpro = 0
        # for i in range(len(prices)):
        #     for  j in range(i,len(prices)):
        #         if prices[j] - prices[i] > maxpro:
        #             maxpro = prices[j] - prices[i]
        buy_cost = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] - buy_cost > max_profit:
                max_profit = prices[i] - buy_cost

            if prices[i] < buy_cost:
                buy_cost = prices[i]
            

        return max_profit

