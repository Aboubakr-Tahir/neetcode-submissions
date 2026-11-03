class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack1)-1,0,-1) : 
            self.stack2.append(self.stack1.pop(-1))
        poped_element = self.stack1.pop(-1)
        for _ in range(len(self.stack2)-1,-1,-1) : 
            self.stack1.append(self.stack2.pop(-1))
        return poped_element

    def peek(self) -> int:

        for _ in range(len(self.stack1)-1,0,-1) : 
            self.stack2.append(self.stack1.pop(-1))
        poped_element = self.stack1[-1]
        for _ in range(len(self.stack2)-1,-1,-1) : 
            self.stack1.append(self.stack2.pop(-1))
        return poped_element

    def empty(self) -> bool:
        if len(self.stack1) != 0 :
            return False 
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()