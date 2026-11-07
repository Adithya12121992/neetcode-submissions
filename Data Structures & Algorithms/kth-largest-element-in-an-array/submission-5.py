class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for elem in nums:
            heapq.heappush(heap, elem)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]