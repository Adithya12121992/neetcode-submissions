class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nlogn
        '''if not nums:
            return False
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]
        return False'''
        return len(nums) != len(set(nums))