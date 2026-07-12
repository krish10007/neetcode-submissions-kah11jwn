class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(profit,maxp)
            else:
                l = r
            
        return maxp