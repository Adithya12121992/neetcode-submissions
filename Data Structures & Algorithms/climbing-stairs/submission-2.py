class Solution:
    def climbStairs(self, n: int) -> int:
        dict1 = {}
        def dfs(i):
            if i<=2:
                return i
            
            if i in dict1:
                return dict1[i]
            dict1[i] = dfs(i-1)+dfs(i-2)
            return dict1[i]
        return dfs(n)