class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = math.inf
        for elem in prices:
            buy = min(buy, elem)
            profit = max(profit, abs(buy-elem))
        return profit