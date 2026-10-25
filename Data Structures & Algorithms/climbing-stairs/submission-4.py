class Solution:
    def climbStairs(self, n: int) -> int:
        dict1 = {}
        def dp(i):
            if i <=2:
                return i
            if i in dict1:
                return dict1[i]
            dict1[i] = dp(i-1)+dp(i-2)
            return dict1[i]
        return dp(n)