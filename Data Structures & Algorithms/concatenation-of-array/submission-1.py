class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = [None]*(2*len(nums))
        for i in range(len(ret)):
            j = i%len(nums)
            ret[i]=nums[j]
        return ret