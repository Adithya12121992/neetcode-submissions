class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = math.inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
        else:
            self.min_val = min(self.min_val, val)
        self.stack.append((self.min_val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_val = self.stack[-1][0] if self.stack else math.inf

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0] if self.stack else math.inf
        
