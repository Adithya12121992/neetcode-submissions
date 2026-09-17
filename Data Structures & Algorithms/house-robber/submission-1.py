class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        dict1 = {}
        def dp(n):
            if n >=len(nums):
                return 0
            if n in dict1:
                return dict1[n]
            dict1[n] = max(dp(n+1), nums[n]+dp(n+2))
            return dict1[n]
        return dp(0)