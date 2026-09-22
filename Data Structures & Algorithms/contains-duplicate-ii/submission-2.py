class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''dict1 = {}
        for idx, elem in enumerate(nums):
            if elem in dict1 and abs(idx-dict1[elem]) <= k:
                return True
            dict1[elem] = idx
        return False'''
        l = r = 0
        window = set()
        while r< len(nums):
            if r-l >k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
            r+=1
        return False