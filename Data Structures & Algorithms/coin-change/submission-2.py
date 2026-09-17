class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dict1 = {}

        def dp(need):
            if need == 0:
                return 0
            if need in dict1:
                return dict1[need]
            res = math.inf
            for coin in coins:
                new_need = need-coin
                if new_need>=0:
                    res = min(res, 1+ dp(new_need))
            dict1[need] = res
            return dict1[need]
        val = dp(amount)
        return val if val!=math.inf else -1