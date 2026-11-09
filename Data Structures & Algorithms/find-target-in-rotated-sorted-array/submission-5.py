class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (r+l)//2
            # find the sub araay where it is rotated and 
            # check if the target is within that rotation sub array
            if nums[mid] == target:
                return mid
            if nums[mid]>nums[r]:
                # if rotated
                if nums[l] <= target < nums[mid]:
                    r= mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]< target<=nums[r]:
                    l = mid+1
                else:
                    r= mid-1
        return -1