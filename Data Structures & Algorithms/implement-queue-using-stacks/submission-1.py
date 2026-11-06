class MyQueue:
    from collections import deque
    def __init__(self):
        self.main_que=deque()

    def push(self, x: int) -> None:
        self.main_que.append(x)

    def pop(self) -> int:
        return self.main_que.popleft()

    def peek(self) -> int:
        return self.main_que[0]

    def empty(self) -> bool:
        return not bool(self.main_que)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()