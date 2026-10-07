class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for idx, elem in enumerate(temperatures):
            if not stack or elem <= stack[-1][0]:
                stack.append((elem, idx))
            else:
                while stack and stack[-1][0] <elem:
                    pop_elem, pop_idx = stack.pop()
                    result[pop_idx] = idx-pop_idx
                stack.append((elem, idx))
        return result
                