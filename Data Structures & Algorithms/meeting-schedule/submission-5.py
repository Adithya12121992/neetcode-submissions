"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        if not intervals:
            return True
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if start<= intervals[i].start < end:
                return False
            start = intervals[i].start
            end = intervals[i].end
        return True