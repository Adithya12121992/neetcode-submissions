class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount ==0:
                return 0
            if amount in memo:
                return memo[amount]
            res = math.inf
            for coin in coins:
                rem_amount = amount - coin
                if rem_amount>=0:
                    res = min(res, 1 + dfs(rem_amount))
            memo[amount] = res
            return memo[amount]
        ncoins = dfs(amount)
        return ncoins if ncoins!=math.inf else -1
