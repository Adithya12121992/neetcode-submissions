class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        profit = -math.inf

        for elem in prices:
            buy = min(buy, elem)
            profit = max((elem-buy), profit)
        return profit