class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append((val, val))
        else:
            current_min = self.items[-1][1]
            self.items.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.items:
            return self.items.pop()
        else: 
            raise IndexError("Cannot pop an empty stack")

    def top(self) -> int:
        if self.items:
            return self.items[-1][0]
        else:
            raise IndexError("Cannot peek an empty stack")

    def getMin(self) -> int:
        if self.items:
            return self.items[-1][1]
        else:
            raise IndexError("Cannot get min of an empty stack")
