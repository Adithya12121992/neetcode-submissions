class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            pivot = (l+r)//2
            # there are 3 conditions 
            # 1 , if the nums[pivot] > nums[r] and if target is within this limit , then move to the right, this means the left array is sorted and right is not, so we need to search in the unsorted array
            # 2 , if the nums[pivot] > nums[r] and if target is not within this boundry , then move to the left and search in the sorted array 
            # 3 if nums[pivot] == target
            if nums[pivot] == target:
                return pivot
            elif nums[l]<=nums[pivot]:
                if nums[l]<= target<nums[pivot]:
                    r = pivot-1
                else:
                    l = pivot+1
            else:
                if nums[pivot] < target <=nums[r]:
                    l = pivot+1
                else:
                    r = pivot-1
        return -1