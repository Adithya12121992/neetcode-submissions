class Solution:
    def rob(self, nums: List[int]) -> int:
        # every step we take have 2 choices
        # 1. Rob the house and go to the i+2 house 
        # 2. Dont rob the house and go to the i+1 house
        memo = {}
        def dp(i):
            if i >=len(nums):
                return 0
            if i not in memo:
                memo[i] = max(dp(i+1), nums[i]+dp(i+2))
            return memo[i]
        return dp(0)

