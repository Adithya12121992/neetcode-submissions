class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for idx, num in enumerate(nums):
            if target-num in dict1:
                return [dict1[target-num], idx]
            else:
                dict1[num] = idx
        