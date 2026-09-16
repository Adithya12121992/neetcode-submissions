class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''res = []
        for elem in nums:
            heapq.heappush(res, -elem)
        for i in range(k-1):
            heapq.heappop(res)
        return -1 * heapq.heappop(res)'''
        # the above solution is n k logn --> as we are iterating n elems and popping using heap for k times ( heappop() is logk )
        # another way is quick select --> just like quick sort
        k = len(nums)-k
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = pivot, nums[p]
            if p>k:
                return quickSelect(l, p-1)
            elif p<k:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums)-1)