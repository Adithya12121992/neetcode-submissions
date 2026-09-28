class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, time_taken in times:
            graph[source].append([destination, time_taken])
        seen = set()
        queue = [[0, k]]
        total_time = 0
        while queue:
            if len(seen) == n:
                return total_time
            interim_time, node = heapq.heappop(queue)
            if node in seen:
                continue
            seen.add(node)
            total_time = max(total_time, interim_time)

            for nei, nei_time in graph[node]:
                heapq.heappush(queue, [interim_time+nei_time, nei])
        if len(seen) == n:
            return total_time
        else:
            return -1
