class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dict1 = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount in dict1:
                return dict1[amount]
            res = math.inf
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dp(amount-coin))
            dict1[amount]=res
            return dict1[amount]
        ret_val = dp(amount)
        return ret_val if ret_val !=math.inf else -1