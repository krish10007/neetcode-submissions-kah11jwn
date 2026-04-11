class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1,len(prices)): #range starts from 1 not 0 
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

#range cant start with 0 as we are looking at prices[i-1] on first step