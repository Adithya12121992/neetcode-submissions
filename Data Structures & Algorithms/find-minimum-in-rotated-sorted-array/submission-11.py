class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            pivot = (l+r)//2
            if nums[pivot]>nums[r]:
                # right is unsorted and left is sorted. So potentially the smallest might be in the right 
                l = pivot+1
            else:
                r = pivot
        return nums[l]