class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for idx, elem in enumerate(nums):
            i = idx+1
            j = len(nums)-1
            while i < j:
                if elem+nums[i]+nums[j] == 0:
                    res.add((elem, nums[i], nums[j]))
                    i+=1
                    j-=1
                elif elem+nums[i]+nums[j] > 0:
                    j-=1
                else:
                    i+=1
        return [[x,y,z] for x,y,z in res]
