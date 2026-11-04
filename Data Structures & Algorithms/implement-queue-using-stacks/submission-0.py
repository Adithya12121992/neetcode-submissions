class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        stack2 = self.stack1[::-1]
        elem = stack2.pop()
        self.stack1 = stack2[::-1]
        return elem

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return True if not self.stack1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()