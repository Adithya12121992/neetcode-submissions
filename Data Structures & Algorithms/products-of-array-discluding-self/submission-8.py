class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = []
        res = [0]*len(nums)
        for idx, elem in enumerate(nums):
            if elem!=0:
                product*=elem
            else:
                zeros.append(idx)
        if len(zeros)>1:
            return res
        elif len(zeros) == 1:
            for i in range(len(res)):
                if i == zeros[-1]:
                    res[i] = product
        else:
            for i in range(len(res)):
                res[i] = product//nums[i]
        return res