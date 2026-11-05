class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            pivot = (l+r)//2
            if nums[pivot]>nums[r]:
                # rotation is on the right
                l = pivot+1
            else:
                # rotation is on the left
                r = pivot
        return nums[l]
