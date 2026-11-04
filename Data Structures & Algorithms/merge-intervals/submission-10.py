class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        for i in range(len(intervals)):
            # check for 2 conditions
            # 1. when they could overlap 
            # 2. when they cannot overlap --> if the curr start is greater then the prev end 
            if not result:
                result.append(intervals[i])
            else:
                if intervals[i][0] > result[-1][1]:
                    result.append(intervals[i])
                else:
                    result[-1][1] = max(result[-1][1], intervals[i][1])
        return result