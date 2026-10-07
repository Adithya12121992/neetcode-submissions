class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for elem in tokens:
            if elem not in operations:
                stack.append(elem)
            else:
                elem1 = int(stack.pop())
                elem2 = int(stack.pop())
                if elem == '+':
                    result = elem2+elem1
                elif elem == '-':
                    result = elem2-elem1
                elif elem == '*':
                    result = elem2*elem1
                elif elem == '/':
                    result = elem2/elem1
                stack.append(result)
        return int(stack[0])