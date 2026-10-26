"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if start <= intervals[i].start < end:
                return False
            start = min(start, intervals[i].start)
            end = max(end, intervals[i].end)
        return True