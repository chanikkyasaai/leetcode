class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        maxprofit = 0
        i = 0
        j = 1
        
        while j < l:
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxprofit = max(maxprofit,profit)
            else:
                i = j
            j+=1
        return maxprofit
