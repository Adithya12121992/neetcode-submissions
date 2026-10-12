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
        '''return len(nums) != len(set(nums))'''
        dict1 = set()
        for elem in nums:
            if elem in dict1:
                return True
            dict1.add(elem)
        return False
