"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # O(n log n) time (sort + heap ops), O(n) space
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x.start)
        result = []
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if not result:
                heapq.heappush(result, (end, [[start, end]]))
            else:
                if result[0][0] <= start:
                    item = heapq.heappop(result)
                    item[1].append([start, end])
                    heapq.heappush(result, (end, item[1]))
                else:
                     heapq.heappush(result, (end, [[start, end]]))
        # schedule will be like the [ schedule[1] for schedule in result ]
        return len(result)