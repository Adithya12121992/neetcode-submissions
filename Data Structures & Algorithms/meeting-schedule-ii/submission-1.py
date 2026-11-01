"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''intervals.sort(key = lambda x: x.start)
        result = []
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            for j in range(len(result)):
                interim_result = result[j]
                if interim_result[-1][1]<=start:
                    interim_result.append([start, end])
                    result[j] = interim_result
                    break
            else:
                result.append([[start, end]])
        return len(result)'''
        intervals.sort(key = lambda x: x.start)
        result = []
        for interval in intervals:
            if not result:
                heapq.heappush(result, interval.end)
                continue
            if result[0] <= interval.start:
                heapq.heappop(result)
                heapq.heappush(result, interval.end)
            else:
                heapq.heappush(result, interval.end)
        return len(result)

            