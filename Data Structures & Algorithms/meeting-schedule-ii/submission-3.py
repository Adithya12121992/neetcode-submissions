"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        result = []
        for interval in intervals:
            if result and result[0] <= interval.start:
                heapq.heappop(result)
            heapq.heappush(result, interval.end)
        return len(result)

            