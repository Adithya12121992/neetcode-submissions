class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack1 and not self.stack2:
            self.stack1.append(x)
        elif self.stack1 and not self.stack2:
            self.stack1.append(x)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(x)

        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        elem = self.stack2.pop()
        return elem        

    def peek(self) -> int:
        if self.stack1 and not self.stack2:
            return self.stack1[0]
        elif not self.stack1 and self.stack2:
            return self.stack2[-1]

    def empty(self) -> bool:
        if len(self.stack2)==0 and len(self.stack1)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()