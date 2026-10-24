class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) == len(set(nums))
        '''nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev == nums[i]:
                return True
            prev = nums[i]
        return False'''
        set1 = set()
        for elem in nums:
            if elem in set1:
                return True
            set1.add(elem)
        return False
                