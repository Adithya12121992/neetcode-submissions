class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_val = -1
        i, j = 0, len(nums)-1
        while i < j:
            sum1 = nums[i]+nums[j]
            if sum1<k:
                max_val = max(max_val, sum1)
                i+=1
            else:
                j-=1
        return max_val