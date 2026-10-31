class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return_list = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if start <= intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            elif intervals[i][0] > end:
                return_list.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        return_list.append([start, end])
        return return_list

