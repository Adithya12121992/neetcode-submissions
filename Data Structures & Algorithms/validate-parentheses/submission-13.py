class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {')':'(', '}':'{', ']':'['}
        for elem in s:
            if elem not in dict1.keys():
                stack.append(elem)
            else:
                if stack and stack[-1] == dict1[elem]:
                    stack.pop()
                else:
                    stack.append(elem)
        return len(stack) == 0