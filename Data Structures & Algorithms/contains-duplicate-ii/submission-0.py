class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}
        for idx, elem in enumerate(nums):
            if elem in dict1 and abs(idx-dict1[elem]) <= k:
                return True
            dict1[elem] = idx
        return False