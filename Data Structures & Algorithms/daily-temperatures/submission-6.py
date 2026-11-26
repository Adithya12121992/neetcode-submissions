class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                prev_idx, prev_temp = stack.pop()
                res[prev_idx] = (idx-prev_idx)
            stack.append((idx, temp))
        return res