class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        if not intervals:
            return result
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # check for 2 conditions
            # 1. when they could overlap 
            # 2. when they cannot overlap --> if the curr start is greater then the prev end 
            if intervals[i][0] > end:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        result.append([start, end])
        return result