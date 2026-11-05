class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')':'(', '}':'{', ']':'['}
        stack = []
        for elem in s:
            if elem not in dict1:
                stack.append(elem)
            else:
                if stack and stack[-1] == dict1[elem]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
        
