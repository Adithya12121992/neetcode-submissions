class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {']':'[', '}':'{', ')':'('}
        for elem in s:
            if elem in dict1:
                if stack and stack[-1] == dict1[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        return len(stack)==0