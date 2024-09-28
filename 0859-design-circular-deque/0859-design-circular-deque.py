class MyCircularDeque:

    def __init__(self, k: int):
        self.que = deque()
        self.size = k
        self.f = -1

    def insertFront(self, value: int) -> bool:
        if self.f == self.size-1:
            return False
        self.que.appendleft(value)
        self.f+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.f == self.size-1:
            return False
        self.que.append(value)
        self.f+=1
        return True

    def deleteFront(self) -> bool:
        if self.f == -1:
            return False
        self.que.popleft()
        self.f-=1
        return True

    def deleteLast(self) -> bool:
        if self.f == -1:
            return False
        self.que.pop()
        self.f-=1
        return True  

    def getFront(self) -> int:
        if self.f == -1:
            return -1
        return self.que[0]

    def getRear(self) -> int:
        if self.f == -1:
            return -1
        return self.que[self.f]

    def isEmpty(self) -> bool:
        if self.f == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.f == self.size-1:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()