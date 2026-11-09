class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1]*len(nums)
        for i in range(len(nums)):
            res = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    res = max(res, result[j]+1)
            result[i] = res
        return max(result)
