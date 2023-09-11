class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP가 아닌 그리디를 이용하였음
        return sum(max(prices[i]-prices[i-1], 0) for i in range(1, len(prices)))