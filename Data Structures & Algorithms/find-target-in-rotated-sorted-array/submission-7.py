class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            pivot = (r+l)//2
            # check if mid == target
            if nums[pivot] == target:
                return pivot
            elif nums[pivot]> nums[r]:
                # rotated sub array
                if nums[l] <= target < nums[pivot]:
                    r = pivot-1
                else:
                    l = pivot+1
            else:
                # unrotated sub array
                if nums[pivot]<target<=nums[r]:
                    l = pivot+1
                else:
                    r = pivot-1
        return -1