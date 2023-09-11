class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1,2,3,4
        maxgap = 0
        min_price = prices[0]
        for price in prices:
            min_price= min(min_price, price)
            maxgap = max(maxgap, price-min_price)
        
        if maxgap < 0:
            return 0
        else:
            return maxgap
        