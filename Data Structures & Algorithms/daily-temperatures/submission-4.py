class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for idx, elem in enumerate(temperatures):
            while stack and stack[-1][1]<elem:
                popped_index, popped_elem = stack.pop()
                result[popped_index] = (idx-popped_index)
            stack.append((idx, elem))
        return result