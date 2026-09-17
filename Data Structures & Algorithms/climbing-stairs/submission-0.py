class Solution:
    def climbStairs(self, n: int) -> int:
        self.dict1 = {}
        return self.dp(n)
    def dp(self, n):
        if n <= 2:
            return n
        if n < 0:
            return 0
        if n in self.dict1:
            return self.dict1[n]
        self.dict1[n] = self.dp(n-1)+self.dp(n-2)
        return self.dict1[n]
