class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0
        for r in range(1, len(prices)):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
        return maxp
            
