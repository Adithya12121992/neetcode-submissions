class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            # check for 2 conditions
            # 1. when they could overlap 
            # 2. when they cannot overlap --> if the curr start is greater then the prev end 
            if start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)
        return result