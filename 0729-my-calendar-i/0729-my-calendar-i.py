class MyCalendar:

    def __init__(self):
        self.pnt = 0
        self.input = [[]]

    def book(self, start: int, end: int) -> bool:
        if self.pnt > 0:
            self.pnt+=1
            if not self.isIntersect(start,end):
                self.input.append([start,end])
                return True
            else:
                return False

        else:
            self.input.append([start, end])
            self.pnt+=1
            return True
    def isIntersect(self, start,end):

        for i in self.input[1:]:
            if (start >= i[0] and start < i[1]) or (end > i[0] and end <= i[1]) or (start>= i[0] and end <= i[1]) or (i[0] >= start and i[1] <= end):
                return True
        return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)