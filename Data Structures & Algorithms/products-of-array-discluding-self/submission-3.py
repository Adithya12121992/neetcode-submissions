class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = self.get_product(nums, False)
        right_product = self.get_product(nums, True)
        for i in range(len(left_product)):
            left_product[i] *=right_product[i]
        return left_product
    
    def get_product(self, nums, reverse):
        product = []
        if reverse:
            nums = nums[::-1]
        for idx, elem in enumerate(nums):
            if idx == 0:
                product.append(1)
            else:
                product.append(product[idx-1]*nums[idx-1])
        if reverse:
            product = product[::-1]
        return product

