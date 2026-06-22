class Solution:
    def findMin(self, nums: List[int]) -> int:
        # intuition is , if the listed is rotated , at some point nums[l] > nums[r]
        l , r = 0, len(nums)-1
        result = math.inf

        while l <=r:
            pivot = (l+r)//2
            if nums[pivot] > nums[r]:
                # list is rotated , ideally it should not be the case, the small is to the right 
                l = pivot+1
            else:
                # the list is not rotated, the small value is to the left
                r = pivot-1
            result = min(result, nums[pivot])
        return result