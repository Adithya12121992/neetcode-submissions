class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        for idx, (start, end) in enumerate(intervals):
            if idx == 0:
                res.append([start, end])
            else:
                if res[-1][1] >= start:
                    res[-1][1] = max(res[-1][1], end)
                else:
                    res.append([start, end])
        return res