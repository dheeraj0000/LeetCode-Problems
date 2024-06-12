class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._shift_stacks()
        return self.stack2.pop()

    def peek(self) -> int:
        self._shift_stacks()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def _shift_stacks(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


myQueue = MyQueue()
myQueue.push(1)    
myQueue.push(2)    
print(myQueue.peek())  
print(myQueue.pop())   
print(myQueue.empty()) 