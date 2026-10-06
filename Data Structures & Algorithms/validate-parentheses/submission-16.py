class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {')':'(', '}':'{', ']':'['}
        for elem in s:
            if elem not in dict1:
                stack.append(elem)
            elif stack and stack[-1] == dict1[elem]:
                stack.pop()
            else:
                return False
        return len(stack) == 0