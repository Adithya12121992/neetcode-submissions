class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)//2
        for elem in nums:
            total_sum-=elem
        return total_sum
