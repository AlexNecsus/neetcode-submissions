class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        if self.minimum:
            if self.minimum[-1] > val:
                self.minimum.append(val)
            else:
                self.minimum.append(self.minimum[-1])
        else:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.minimum.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum[-1]
        else:
            return int()