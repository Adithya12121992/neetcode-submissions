class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_val = math.inf

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        self.min_stack.append((self.min_val, val))

    def pop(self) -> None:
        self.min_stack.pop()
        self.min_val = self.min_stack[-1][0] if self.min_stack else math.inf
        
    def top(self) -> int:
        return self.min_stack[-1][1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
