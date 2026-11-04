class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # check if the newInterval lesser than the current start , end 
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            # check if the newInterval overlaps
            elif newInterval[0] <= intervals[i][1]:
                newInterval = [ min(newInterval[0], intervals[i][0]), 
                                max(newInterval[1], intervals[i][1]) ]
            # check if the newInterval geater than the current start , end 
            else:
                result.append(intervals[i])
        result.append(newInterval)
        return result