class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''left_product = self.get_product(nums, False)
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
        return product'''
        zero_cnt = []
        product = 1
        return_list = [0]*len(nums)
        for idx, elem in enumerate(nums):
            if elem ==0:
                zero_cnt.append(idx)
            else:
                product*=elem
        
        if len(zero_cnt) >1:
            return return_list
        elif len(zero_cnt) == 1:
            return_list[zero_cnt[-1]] = product
            return return_list
        else:
            for i, elem in enumerate(nums):
                return_list[i] = product//nums[i]
            return return_list
