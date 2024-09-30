class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.maxSize = maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top +1 == self.maxSize:
            return
        else:
            self.stack.append(x)
            self.top+=1

    def pop(self) -> int:
        if self.top == -1:
            return -1
        else:
            self.top-=1
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if self.top+1 <= k:
            for i in range(self.top+1):
                self.stack[i]+= val
        else:
            for i in range(k):
                self.stack[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)