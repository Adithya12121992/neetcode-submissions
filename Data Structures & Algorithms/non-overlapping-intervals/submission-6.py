class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        cnt = 0
        intervals.sort()
        start = intervals[0][0]
        end   = intervals[0][1]
        for i in range(1, len(intervals)):
            # check start of the current interval is less than the previous
            if intervals[i][0] < end:
                end = min(end, intervals[i][1])
                cnt+=1
            else:
                start = intervals[i][0]
                end = intervals[i][1]
        return cnt
        