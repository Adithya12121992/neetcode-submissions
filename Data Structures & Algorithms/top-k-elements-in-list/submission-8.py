class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for elem in nums:
            dict1[elem]+=1
        res = []
        for key, val in dict1.items():
            heapq.heappush(res,(val, key))
            if len(res)>k:
                heapq.heappop(res)
        return [x[1] for x in res]
        