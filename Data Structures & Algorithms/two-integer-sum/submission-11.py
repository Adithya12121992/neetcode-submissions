class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for idx, elem in enumerate(nums):
            if (target-elem) in dict1:
                return [dict1[(target-elem)], idx]
            dict1[elem]=idx
        