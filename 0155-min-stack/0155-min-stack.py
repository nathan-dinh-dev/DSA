class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.insert(0, val)
        # return null

    def pop(self) -> None:
        self.st.pop(0)
        # return null

    def top(self) -> int:
        return self.st[0]

    def getMin(self) -> int:
        return min(self.st)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()