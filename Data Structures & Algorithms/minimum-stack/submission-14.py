class MinStack:

    def __init__(self):
        self.stack = []
        self.minimal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimal and val <= self.minimal[-1] : 
            self.minimal.append(val)
        elif not self.minimal : 
            self.minimal.append(val)

    def pop(self) -> None:
        if self.minimal and self.stack[-1] == self.minimal[-1] :
            self.stack.pop(-1)
            self.minimal.pop(-1)
        else : 
            self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimal[-1]
