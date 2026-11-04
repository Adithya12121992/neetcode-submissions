class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # check if newInrerval is lesser than the current interval
            if newInterval[1]< intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            # if current interval is lesser than newInterval
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            # if there is an overlap
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
        result.append(newInterval)
        return result