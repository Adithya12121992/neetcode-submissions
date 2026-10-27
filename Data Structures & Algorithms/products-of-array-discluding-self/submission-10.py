class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = self.find_product(nums, False)
        right_product = self.find_product(nums, True)
        for i in range(len(left_product)):
            left_product[i]*=right_product[i]
        return left_product
    def find_product(self, nums, reverse=False):
        if reverse:
            nums = nums[::-1]
        result = [1]
        for i in range(1, len(nums)):
            result.append(nums[i-1]*result[i-1])
        if reverse:
            return result[::-1]
        return result