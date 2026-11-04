"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # basically thre intuition is to keep track of the start and the end times.
        # compare the current start with previous end for overlaps 
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True