class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return_set = set()
        for idx, elem in enumerate(nums):
            i = idx+1
            j = len(nums)-1
            while i < j:
                if elem + nums[i] + nums[j] == 0:
                    return_set.add((elem , nums[i], nums[j]))
                    i+=1
                    j-=1
                elif elem + nums[i] + nums[j] < 0:
                    i+=1
                elif elem + nums[i] + nums[j] > 0:
                    j-=1
        return [list(x) for x in return_set]