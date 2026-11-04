class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif newInterval[0] <= intervals[i][1]:
                newInterval = [ min(newInterval[0], intervals[i][0]), 
                                max(newInterval[1], intervals[i][1]) ]
            else:
                result.append(intervals[i])
        result.append(newInterval)
        return result