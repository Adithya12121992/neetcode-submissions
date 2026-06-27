class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Adithya Solution
        left = self.prodct(nums)
        reverse = nums[::-1]
        right = self.prodct(reverse, True)
        res = []
        for i in range(len(left)):
            res.append(left[i]*right[i])
        return res
    def prodct(self, nums1, reverse=False):
        product = [1]
        for i in range(len(nums1)):
            if i == 0:
                continue
            product.append(product[i-1]*nums1[i-1])
        if not reverse:
            return product
        else:
            return product[::-1]