class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set(nums)
        for i in range(1, len(nums)+1):
            if i not in set1:
                return i
        return 0