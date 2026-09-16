class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for elem in nums:
            heapq.heappush(res, -elem)
        for i in range(k-1):
            heapq.heappop(res)
        return -1 * heapq.heappop(res)