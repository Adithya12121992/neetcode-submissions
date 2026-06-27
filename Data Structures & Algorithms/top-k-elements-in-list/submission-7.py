class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for elem in nums:
            dict1[elem]+=1
        ret = []
        for key, val in dict1.items():
            heapq.heappush(ret, (val, key))
            if len(ret) > k:
                heapq.heappop(ret)
        return [x[1] for x in ret]
