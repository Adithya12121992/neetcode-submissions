class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''result = []
        intervals.append(newInterval)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end , intervals[i][1])
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result'''
        result = []
        i = 0
        n = len(intervals)
        newInterval = list(newInterval)
        # phase 1 : lesser intervals than new addition
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        # phase 2: 
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result