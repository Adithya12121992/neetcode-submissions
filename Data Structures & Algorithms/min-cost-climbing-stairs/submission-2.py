class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dict1 = {}
        def dp(n):
            
            if n >= len(cost):
                return 0
            if n in dict1:
                return dict1[n]
            dict1[n] = cost[n]+ min(dp(n+1), dp(n+2))
            return dict1[n]
        return min(dp(0), dp(1))