class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            pivot  = (l+r)//2
            print(nums[l], nums[r], nums[pivot])
            # now , we have 2 cases 
            # 1 if the nums[pivot] > nums[r], in that case the number is rotated , so the smallest element is on the right
            # else the smallest number is on the left 
            if nums[pivot]>nums[r]:
                l = pivot+1
            else:
                r = pivot
        return nums[l]