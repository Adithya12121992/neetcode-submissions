class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num]+=1
        result = []
        for key, val in dict1.items():
            heapq.heappush(result, (val, key))
            if len(result) >k:
                heapq.heappop(result)
        return [x[1] for x in result]
