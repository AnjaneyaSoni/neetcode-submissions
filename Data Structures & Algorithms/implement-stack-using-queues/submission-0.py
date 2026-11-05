class MyStack:

    def __init__(self):
        self.lifo=[]

    def push(self, x: int) -> None:
        self.lifo.append(x)

    def pop(self) -> int:
        temp=self.lifo[-1]
        del self.lifo[-1]
        return temp

    def top(self) -> int:
        return self.lifo[-1]

    def empty(self) -> bool:
        return False if self.lifo else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()