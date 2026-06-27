class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Adithya Solution, O(n), O(n)
        dict1 = {}
        for idx, elem in enumerate(nums):
            if (target-elem) in dict1.keys():
                return [dict1[target-elem],idx]
            else:
                dict1[elem] = idx