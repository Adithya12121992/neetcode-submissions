class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'}':'{', ']':'[', ')':'('}
        stack = []
        for elem in s:
            if elem in dict1:
                if stack and stack[-1] == dict1[elem]:
                    stack.pop()
                    continue
            stack.append(elem)
        return len(stack)==0
